import json
import os
import stat
from datetime import datetime, timezone


class StaffManager:
    # ---- Reusable Table Header ----
    table_header = f"{'ID':<10} {'First Name':<13} {'Last Name':<13} {'Department':<15} {'Position':<15} {'Role':<15} {'Salary':<10} {'Joined Date':<12}"
    divider = "=" * 120

    def __init__(self):
        self.staff = []
        self.data_file = "staff.json"
        self.next_id = 1  # Helps to generate unique IDs for new staff members
        self.load_data()  # Load existing staff data from the JSON file if it exists

    # --- Data Persistence ---
    def load_data(self):
        """Loads staff data from the JSON file if it exists and handles missing or corrupted files."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as file:
                    content = file.read()
                    if content.strip():  # Check if the file is not empty
                        data = json.loads(content)
                        self.staff = data.get("staff", [])
                        self.next_id = data.get("next_id", 1)

                        os.chmod(
                            self.data_file, stat.S_IRUSR | stat.S_IWUSR
                        )  # Set file permissions to read/write for the owner only (600)

                        print(
                            f"Loaded {len(self.staff)} staff members from {self.data_file}."
                        )
                    else:
                        print("Empty file found. Starting fresh.")
            except json.JSONDecodeError:
                print(
                    f"Error: {self.data_file} is corrupted. Starting with an empty staff list."
                )
        else:
            print(
                f"File {self.data_file} not found. Starting with an empty staff list."
            )

    def save_data(self):
        """Saves the current staff data to the JSON file with restricted file permissions."""
        data = {"staff": self.staff, "next_id": self.next_id}

        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            # Set file permissions to read/write for the owner only (600)
            os.chmod(self.data_file, stat.S_IRUSR | stat.S_IWUSR)
            print("Data saved successfully.")
        except PermissionError:
            print("Error: Permission denied. Unable to save data.")
        except OSError as e:
            print(f"Error saving data: {e}")

    def _print_table(self, members):
        """Reusable method to print a formatted table of staff members."""
        print(self.table_header)
        print(self.divider)
        for member in members:
            print(
                f"{member['id']:<10} {member['first_name']:<13} {member['last_name']:<13}"
                f"{member['department']:<15} {member['position']:<15} {member['role']:<15}"
                f"{member['salary']:<10} {member['joined_date']:<12}"
            )
        print(self.divider)

    # ---Staff Operations---
    def add_staff(self, first_name, last_name, department, position, role, salary):
        # Generate a unique ID for the new staff member
        staff_id = f"STF{self.next_id:04d}"  # Format the ID with leading zeros (e.g., STF0001, STF0002, etc.)
        self.next_id += 1  # Increment the next_id for future staff members

        staff_member = {
            "id": staff_id,
            "first_name": first_name,
            "last_name": last_name,
            "department": department,
            "position": position,
            "role": role,
            "salary": salary,
            "joined_date": datetime.now(timezone.utc).strftime(
                "%Y-%m-%d"
            ),  # Store the date when the staff member was added
        }
        self.staff.append(staff_member)
        print(
            f"Staff member {first_name} {last_name} added successfully with ID {staff_id}, department: {department} , position: {position} , role: {role} , salary: {salary} ."
        )
        self.save_data()

    def list_staff(self):
        if not self.staff:
            print("No staff members found.")
            return

        print("\n===== STAFF DIRECTORY =====")
        self._print_table(self.staff)

    def search_staff(self, search_term):
        term = search_term.lower()
        # Search for staff members by ID, name, department, position, or role (case-insensitive)
        results = [
            member
            for member in self.staff
            if any(
                term in str(member[k]).lower()
                for k in (
                    "id",
                    "first_name",
                    "last_name",
                    "department",
                    "position",
                    "role",
                )
            )
        ]

        if results:
            print(f"\n===== SEARCH RESULTS FOR '{search_term}' =====")
            self._print_table(results)
        else:
            print(f"No staff members found matching '{search_term}'.")

    UPDATABLE_FIELDS = (
        "first_name",
        "last_name",
        "department",
        "position",
        "role",
        "salary",
    )

    def _find_member(self, staff_id):
        """Return the member dict with this ID (case insensitive), or None."""
        for member in self.staff:
            if member["id"].lower() == staff_id.lower():
                return member
            return None

    def update_staff(self, staff_id):
        """Find a staff member by ID and update one whitelisted field."""
        # Locate the record
        target = None
        for member in self.staff:
            if member["id"].lower() == staff_id.lower():
                target = member
                break

        # Handle "Not Found"
        if not target:
            print(f"\n No staff member found with ID {staff_id}.")
            return

        # Show current values before editing
        print(
            f"\n Editing {target['first_name']} {target['last_name']} ({target['id']})"
        )
        print("-" * 50)
        for key, value in target.items():
            print(f" {key}: {value}")

        print("\nUpdatable Fields:", ", ".join(self.UPDATABLE_FIELDS))
        field = input("Which field to update? ").strip().lower()

        if field not in self.UPDATABLE_FIELDS:  # whitelist gate
            print("[!] Invalid field. Nothing was changed.")
            return

        value = input(f"New value for '{field}': ").strip()
        if not value:
            print("[!] Value cannot be empty. Nothing was changed.")
            return

        if field == "salary":  # type-specific validation
            try:
                value = float(value)
                if value < 0:
                    print("[!] Salary cannot be negative. Nothing was changed.")
                    return
            except ValueError:
                print("[!] Salary must be a number. Nothing was ")
                return

        target[field] = value  # Edits self.staff
        self.save_data()
        print(
            f"[+] Updated {field.upper()} for {target['first_name']} {target['last_name']}."
        )


# ---- Main Program Loop ----
def main():
    manager = StaffManager()

    while True:
        print("\n===== STAFF MANAGEMENT SYSTEM =====")
        print("1. Add Staff Member")
        print("2. List All Staff Members")
        print("3. Search Staff Member")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Validate all inputs to ensure they are not empty
            first_name = input("Enter first name: ").strip()
            if not first_name:
                print("First name cannot be empty. Please try again.")
                continue  # Skip to the next iteration of the loop if name is empty

            last_name = input("Enter last name: ").strip()
            if not last_name:
                print("last name cannot be empty.")
                continue

            department = input("Enter department: ").strip()
            if not department:
                print("Department cannot be empty. Please try again.")
                continue

            position = input("Enter position: ").strip()
            if not position:
                print("Position cannot be empty. Please try again.")
                continue

            role = input("Enter role: ").strip()
            if not role:
                print("Role cannot be empty. Please try again.")
                continue

            # Validate salary input to ensure it's a numeric value and not negative
            try:
                salary = float(input("Enter salary: "))
            except ValueError:
                print("Invalid salary input. Please enter a numeric value.")
                continue

            if salary < 0:
                print("Salary cannot be negative. Please enter a valid salary.")
                continue

            manager.add_staff(first_name, last_name, department, position, role, salary)

        elif choice == "2":
            manager.list_staff()

        elif choice == "3":
            # Validate search term input to ensure it's not empty
            search_term = input(
                "Enter ID, name, department, position, or role to search: "
            ).strip()
            if not search_term:
                print("Search term cannot be empty. Please try again.")
                continue
            manager.search_staff(search_term)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
