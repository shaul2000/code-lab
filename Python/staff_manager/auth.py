import json
import os
import stat
from datetime import UTC, datetime, timedelta

import bcrypt


class AuthManager:
    MAX_ATTEMPTS = 3
    LOCKOUT_MINUTES = 15
    MIN_PASSWORD_LENGTH = 8

    def __init__(self):
        self.auth_file = "auth.json"
        self.is_authenticated = False
        self.users = {}
        self.load_auth()

    # --- Persistence (atomic writes, same pattern as StaffManager) ---
    def load_auth(self):
        if os.path.exists(self.auth_file):
            try:
                with open(self.auth_file, "r", encoding="utf-8") as file:
                    content = file.read()

                if content.strip():
                    self.users = json.loads(content)
                    os.chmod(self.auth_file, stat.S_IRUSR | stat.S_IWUSR)

            except json.JSONDecodeError:
                print("[!] auth.json is corrupted. Starting fresh.")
                self.users = {}

    def save_auth(self):
        tmp = self.auth_file + ".tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as file:
                json.dump(self.users, file, indent=4)
            os.replace(tmp, self.auth_file)
            os.chmod(self.auth_file, stat.S_IRUSR | stat.S_IWUSR)
        except OSError as e:
            print(f"[!] Could not save auth data: {e}")
            try:
                os.unlink(tmp)
            except FileNotFoundError:
                pass

    # Password helpers:
    @staticmethod
    def _hash_password(password):
        """bcrypt auto-generates a unique salt per hash."""
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def _verify_password(password, stored_hash):
        try:
            return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
        except ValueError:
            return False

    @staticmethod
    def _password_is_strong(password):
        if len(password) < AuthManager.MIN_PASSWORD_LENGTH:
            return False, f"Password must be at least {AuthManager.MIN_PASSWORD_LENGTH} characters."
        if password.isalpha() or password.isdigit():
            return False, "Password must mix letters and numbers."
        return True, ""

    # Account setup
    def need_setup(self):
        return not self.users

    def create_admin(self, username, password):
        ok, msg = self._password_is_strong(password)
        if not ok:
            print(f"[!] {msg}")
            return False

        if username.lower() in self.users:
            print(f"[!] Admin account '{username}' already exists.")
            return False

        self.users[username.lower()] = {
            "username": username,
            "password_hash": self._hash_password(password),
            "failed_attempts": 0,
            "locked_until": None,
            "created_at": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.save_auth()
        print(f"[+] Admin account '{username}' created.")
        return True

    # Lockout Logic:
    def _is_locked(self, user):
        if not user.get("locked_until"):
            return False

        locked_until = datetime.strptime(user["locked_until"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
        if datetime.now(UTC) >= locked_until:
            user["locked_until"] = None
            user["failed_attempts"] = 0
            return False
        return True

    # Login:
    def login(self, username, password):
        user = self.users.get(username.lower())
        if not user:
            print("[!] Invalid username or password.")
            return False

        if self._is_locked(user):
            print(f"[!] Account locked until {user['locked_until']}.")
            return False

        if self._verify_password(password, user["password_hash"]):
            user["failed_attempts"] = 0
            user["locked_until"] = None
            self.save_auth()
            self.is_authenticated = True
            print(f"[+] Welcome back, {user['username']}.")
            return True

        user["failed_attempts"] += 1
        remaining = self.MAX_ATTEMPTS - user["failed_attempts"]
        if remaining <= 0:
            user["locked_until"] = (datetime.now(UTC) + timedelta(minutes=self.LOCKOUT_MINUTES)).strftime("%Y-%m-%d %H:%M:%S")
            user["failed_attempts"] = 0
            print(f"[!] Too many failed attempts. Account locked for {self.LOCKOUT_MINUTES} minutes")
            
        else:
            print(f"[!] Invalid username or password. {remaining} attempts remaining.")

        self.save_auth()
        return False

    