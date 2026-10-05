import json
import os
import stat
from datetime import datetime, timezone


class StaffManager:
    # ---- Reusable Table Header ----
    table_header = f"{'ID':<10} {'Name':<20} {'Department':<15} {'Position':<15} {'Role':<15} {'Salary':<10} {'Joined Date':<12}"
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
                f"{member['id']:<10} {member['name']:<20} {member['department']:<15} {member['position']:<15} {member['role']:<15} {member['salary']:<10} {member['joined_date']:<12}"
            )
        print(self.divider)

    # ---Staff Operations---
    def add_staff(self, name, department, position, role, salary):
        # Generate a unique ID for the new staff member
        staff_id = f"STF{self.next_id:04d}"  # Format the ID with leading zeros (e.g., STF0001, STF0002, etc.)
        self.next_id += 1  # Increment the next_id for future staff members

        staff_member = {
            "id": staff_id,
            "name": name,
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
            f"Staff member {name} added successfully with ID {staff_id}, department: {department} , position: {position} , role: {role} , salary: {salary} ."
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
                for k in ("id", "name", "department", "position", "role")
            )
        ]

        if results:
            print(f"\n===== SEARCH RESULTS FOR '{search_term}' =====")
            self._print_table(results)
        else:
            print(f"No staff members found matching '{search_term}'.")


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
            name = input("Enter staff member's name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue  # Skip to the next iteration of the loop if name is empty

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

            manager.add_staff(name, department, position, role, salary)

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
