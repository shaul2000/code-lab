from app import get_password


def staff_dashboard(manager, auth, session):
    """Staff portal: view profile, edit own details, change password."""
    while True:
        print("\n==== MY DASHBOARD ====")
        print("1. View My Profile")
        print("2. Edit my Details")
        print("3. Change Password")
        print("4. Logout")
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            manager.view_own_profile(session.get("staff_code"))
        elif choice == "2":
            manager.edit_own_profile(session.get("staff_code"))
        elif choice == "3":
            old_pw = get_password("Current password: ")
            new_pw = get_password("New password: ")
            auth.change_password(session["username"], old_pw, new_pw)
        elif choice == "4":
            print("[!] Logged out.")
            return
        else:
            print("[!] Invalid choice.")