import json
import math
import os
import re
import stat
from datetime import UTC, datetime


class StaffManager:
    # ---- Reusable Table Header ----
    table_header = f"{'ID':<10} {'First Name':<13} {'Last Name':<13} {'Department':<15} {'Position':<15} {'Role':<15} {'Salary':<10} {'Joined Date':<20}"
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
                        
                        # Recalculate next_id from actual data + stored value (never trust either alone)
                        existing_ids = []
                        for m in self.staff:
                            raw_id = str(m.get("id", ""))
                            if raw_id.startswith("STF"):
                                num_part = raw_id[3:] # Remove "STF"
                                try:
                                    existing_ids.append(int(num_part))
                                except ValueError:
                                    print(f"[!] Skipping record with malformed ID: {raw_id}")
                                    
                        stored_next = data.get("next_id", 1)
                        self.next_id = max((stored_next, max(existing_ids) if existing_ids else 0)) + 1

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
        tmp = self.data_file + ".tmp"

        try:
            with open(tmp, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            os.replace(tmp, self.data_file)  # Atomic swap
            # Set file permissions to read/write for the owner only (600)
            os.chmod(self.data_file, stat.S_IRUSR | stat.S_IWUSR)
            print("Data saved successfully.")
        except PermissionError:
            print("Error: Permission denied. Unable to save data.")
            
            try:
                os.unlink(tmp)
            except FileNotFoundError:
                pass
        except OSError as e:
            print(f"Error saving data: {e}")
            try:
                os.unlink(tmp)
            except FileNotFoundError:
                pass

    def _print_table(self, members):
        """Reusable method to print a formatted table of staff members."""
        print(self.table_header)
        print(self.divider)
        for member in members:
            print(
                f"{member['id']:<10} {member['first_name']:<13} {member['last_name']:<13}"
                f"{member['department']:<15} {member['position']:<15} {member['role']:<15}"
                f"{member['salary']:<10} {member['joined_date']:<20}"
            )
        print(self.divider)

    # ---Staff Operations---
    def _validate_text_field(self, value, field_name, max_length=100):
        """Normalize, strip HTML, and validate required text fields."""
        if value is None:
            raise ValueError(f"{field_name} cannot be empty.")

        normalized = str(value).strip()
        if not normalized:
            raise ValueError(f"{field_name} cannot be empty.")
        
        normalized = re.sub(r'<[^>]+>', '', normalized) # Strip HTML tags
        if not normalized:
            raise ValueError(f"{field_name} contains only HTML tags.")
        
        if len(normalized) > max_length:
            raise ValueError(f"{field_name} exceeds {max_length} characters.")
        return normalized

    def _coerce_salary(self, value):
        """Validate salary input and return a float."""
        try:
            salary = float(value)
        except (TypeError, ValueError):
            raise ValueError("Salary must be a number.") from None

        if not math.isfinite(salary):
            raise ValueError("Salary must be a finite number.")

        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        return float(salary)

    def add_staff(self, first_name, last_name, department, position, role, salary):
        # Generate a unique ID for the new staff member
        try:
            first_name = self._validate_text_field(first_name, "First name", max_length=50)
            last_name = self._validate_text_field(last_name, "Last name", max_length=50)
            department = self._validate_text_field(department, "Department")
            position = self._validate_text_field(position, "Position")
            role = self._validate_text_field(role, "Role")
            salary = self._coerce_salary(salary)
        except ValueError as exc:
            print(f"[!] {exc} Nothing was added.")
            return

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
            "joined_date": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S"),  # Store the date when the staff member was added 
        }
        self.staff.append(staff_member)
        print(
            f"Staff member {first_name} {last_name} added successfully with ID {staff_id}, department: {department} , position: {position} , role: {role} , salary: {salary} ."
        )
        self.save_data()

    def list_staff(self):
        active = self._get_active_only()
        if not active:
            print("No staff members found.")
            return

        print("\n===== STAFF DIRECTORY =====")
        self._print_table(active)

    def search_staff(self, search_term):
        if search_term is None:
            print("Search term cannot be empty.")
            return

        term = str(search_term).strip().lower()
        if not term:
            print("Search term cannot be empty.")
            return

        # Search for staff members by ID, name, department, position, or role (case-insensitive)
        active = self._get_active_only()
        results = [
            member
            for member in active
            if any(
                term in str(member.get(k, "")).lower()
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
        if staff_id is None:
            return None

        normalized_id = str(staff_id).strip()
        if not normalized_id:
            return None

        for member in self.staff:
            member_id = str(member.get("id", ""))
            if member_id.lower() == normalized_id.lower():
                return member
        return None
    
    def _get_active_only(self):
        """Filter out soft-deleted records."""
        return [m for m in self.staff if m.get("active", True)]

    def update_staff(self, staff_id):
        """Find a staff member by ID and update one whitelisted field."""
        # Locate the record
        target = self._find_member(staff_id)

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
        
        if field == "role":
            confirm = input("[!] Changing role is admin-only action. Confirm? [y/N]: ").strip().lower()
            if confirm != 'y':
                print("[i] Role change cancelled.")
                return
                

        value = input(f"New value for '{field}': ").strip()
        if not value:
            print("[!] Value cannot be empty. Nothing was changed.")
            return

        if field == "salary":  # type-specific validation
            try:
                value = self._coerce_salary(value)
            except ValueError as exc:
                print(f"[!] {exc} Nothing was changed.")
                return

        else:
            try:
                value = self._validate_text_field(value, field.replace("_", " ").title())
            except ValueError as exc:
                print(f"[!] {exc} Nothing was changed.")
                return

        target[field] = value  # Edits self.staff
        self.save_data()
        print(
            f"[+] Updated {field.upper()} for {target['first_name']} {target['last_name']}."
        )

    def delete_staff(self, staff_id):
        """Soft-delete a staff member by ID after explicit confirmation."""
        target = self._find_member(staff_id)

        if not target:
            print(f"\n[!] No staff member found with ID {staff_id}.")
            return

        self._print_table([target])
        confirm = (
            input(
                f"Permanently delete {target['first_name']} {target['last_name']} "
                f"({target['id']})? [y/N]: "
            )
            .strip()
            .lower()
        )

        if confirm != "y":  # Silence means No (fail-safe)
            print("[i] Delete cancelled. Nothing was removed.")
            return
        target["active"] = False
        target["deleted_at"] = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
        self.save_data()
        print(f"[+] Deleted {target['first_name']} {target['last_name']} ({target['id']}).")


# ---- Main Program Loop ----
def main():
    manager = StaffManager()

    while True:
        print("\n===== STAFF MANAGEMENT SYSTEM =====")
        print("1. Add Staff Member")
        print("2. List All Staff Members")
        print("3. Search Staff Member")
        print("4. Update Staff Member")
        print("5. Delete Staff Member")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid choice. Please try again.")
            continue

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
            staff_id = input("Enter staff ID to update: ").strip()
            manager.update_staff(staff_id)

        elif choice == "5":
            staff_id = input("Enter staff ID to delete: ").strip()
            manager.delete_staff(staff_id)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
