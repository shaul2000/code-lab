"""Shared helpers used across the staff manager application."""
import getpass

def get_password(prompt="Password: "):
    """Ask for password with optional reveal and confirm."""
    while True:
        password = getpass.getpass(prompt)
        if not password:
            print("[!] Password cannot be empty.")
            continue

        reveal = input("Reveal password? [y/N]: ").strip().lower()
        if reveal == "y":
            print(f"[+] Password entered: {password}")

        confirm = input("Confirm password: [Y/n]: ").strip().lower()
        if confirm == "n":
            print("[!] Password confirmation failed. Please try again.")
            continue
        return password