import json
import os
import stat
from datetime import UTC, datetime, timedelta

import bcrypt


class AuthManager:
    MAX_ATTEMPTS = 3
    LOCKOUT_MINUTES = 15
    MIN_PASSWORD_LENGTH = 12 

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
                    
                else:
                    print("[!] auth.json is empty, Starting fresh.")
                    self.users = {}

            except json.JSONDecodeError:
                raise RuntimeError("auth.json is corrupted Restore a backup or fix it manually. Refusing to start.")
        else:
            print("[+] No auth file found. Starting fresh.")
            self.users = {}
            
    def save_auth(self):
        tmp = self.auth_file + ".tmp"
        # cspell:disable-next-line
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as file:
                json.dump(self.users, file, indent=4)
                file.flush()
                os.fsync(file.fileno())
            os.replace(tmp, self.auth_file)
        except OSError as e:
            print(f"[!] Could not save auth data: {e}")
            try:
                os.unlink(tmp)
            except FileNotFoundError:
                pass

    # Password helpers
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
        
        if not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter."
        
        if not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter."
        
        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one number."
        
        if not any(c in "!@#$%^&*()_+-=" for c in password):
            return False, "Password must contain at least one special character."
        
        return True, ""

    # Account setup
    def need_setup(self):
        return not any(user.get("role") == "admin" for user in self.users.values())

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
            "role": "admin",
            "failed_attempts": 0,
            "locked_until": None,
            "created_at": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.save_auth()
        print(f"[+] Admin account '{username}' created.")
        return True

    # Lockout logic
    def _is_locked(self, user):
        if not user.get("locked_until"):
            return False

        locked_until = datetime.strptime(user["locked_until"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
        if datetime.now(UTC) >= locked_until:
            user["locked_until"] = None
            user["failed_attempts"] = 0
            return False
        return True

    def _register_failure(self, user):
        """Track shared failed attempts for login and password changes."""
        user["failed_attempts"] += 1
        remaining = self.MAX_ATTEMPTS - user["failed_attempts"]
        if remaining <= 0:
            user["locked_until"] = (datetime.now(UTC) + timedelta(minutes=self.LOCKOUT_MINUTES)).strftime("%Y-%m-%d %H:%M:%S")
            print(f"[!] Too many failed attempts. Account locked for {self.LOCKOUT_MINUTES} minutes.")
        else:
            print(f"[!] Invalid username or password. {remaining} attempt(s) remaining.")
        self.save_auth()

    # Login
    def login(self, username, password):
        user = self.users.get(username.lower())
        if not user:
            print("[!] Invalid username or password.")
            return None

        if self._is_locked(user):
            print(f"[!] Account locked until {user['locked_until']}.")
            return None

        if self._verify_password(password, user["password_hash"]):
            user["failed_attempts"] = 0
            user["locked_until"] = None
            self.save_auth()
            self.is_authenticated = True
            print(f"[+] Welcome back, {user['username']}.")
            return dict(user)

        self._register_failure(user)
        return None

    # Change password
    def change_password(self, username, old_password, new_password):
        user = self.users.get(username.lower())
        if not user:
            print("[!] Invalid username or password.")
            return False

        if self._is_locked(user):
            print(f"[!] Account locked until {user['locked_until']}.")
            return False

        if not self._verify_password(old_password, user["password_hash"]):
            self._register_failure(user)
            return False

        ok, msg = self._password_is_strong(new_password)
        if not ok:
            print(f"[!] {msg}")
            return False

        if old_password == new_password:
            print("[!] New password must be different from the current password.")
            return False

        user["password_hash"] = self._hash_password(new_password)
        user["failed_attempts"] = 0
        user["locked_until"] = None
        self.save_auth()
        print(f"[+] Password updated for {user['username']}.")
        return True
    
    def create_staff_user(self, staff_code, username, temp_password):
        """Create a login linked to a specific staff record."""
        self.users[username.lower()] = {
            "username": username,
            "password_hash": self._hash_password(temp_password),
            "role": "staff",
            "staff_code": staff_code,
            "failed_attempts": 0,
            "locked_until": None,
            "must_change_pw": True,
            "created_at": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S"),            
        }
        self.save_auth()
        print(f"[+] Login created for {staff_code}: username '{username}'")
        return True
    
 