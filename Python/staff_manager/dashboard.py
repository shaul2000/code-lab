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
            pass #TODO: call manger.view_own_profile(session)
        elif choice == "2":
            pass #TODO: call manager.edit_own_profile(session)
        elif choice == "3":
            pass #TODO: handle password change
        elif choice == "4":
            print("[!] Logged out.")
            return
        else:
            print("[!] Invalid choice.")