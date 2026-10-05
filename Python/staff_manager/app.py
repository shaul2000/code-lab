import json
import os
from datetime import datetime

class StaffManager:
    def __init__(self):
        self.staff = []
        self.data_file = "staff.json"
        self.next_id = 1 # Helps to generate unique IDs for new staff members
        self.load_data()    # Load existing staff data from the JSON file if it exists
    
    #--- Data Persistence ---    
    def load_data(self):
        """Loads staff data from the JSON file if it exists and handles missing or corrupted files."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding = "utf-8") as file:
                    content = file.read()
                    if content.strip():  # Check if the file is not empty
                        data = json.loads(content)
                        self.staff = data.get("staff", [])
                        self.next_id = data.get("next_id", 1)
                        print(f"Loaded {len(self.staff)} staff members from {self.data_file}.")
                    else:
                        print(f"Empty file found. Starting fresh.")
            except json.JSONDecodeError:
                print(f"Error: {self.data_file} is corrupted. Starting with an empty staff list.")
        else:
            print(f"File {self.data_file} not found. Starting with an empty staff list.")
            
    def save_data(self):
        """Saves the current staff data to the JSON file."""
        data = {
            "staff": self.staff,
            "next_id": self.next_id
        }
        with open(self.data_file, "w", encoding = "utf-8") as file:
            
            json.dump(data, file, indent=4)
        print(f"Data saved successfully.")
    
    # ---Staff Operations---
    def add_staff(self, name, department, position, role,  salary):
        # Generate a unique ID for the new staff member
        staff_id = f"STF{self.next_id:04d}" # Format the ID with leading zeros (e.g., STF0001, STF0002, etc.)
        self.next_id += 1  # Increment the next_id for future staff members
        
        staff_member = {
            "id": staff_id,
            "name": name,
            "department": department,
            "position": position,
            "role": role,
            "salary": salary
        }
        self.staff.append(staff_member)
        print (f"Staff member {name} added successfully with ID {staff_id}, department: {department} , position: {position} , role: {role} , salary: {salary} .")
        self.save_data()
        
    def list_staff(self):
        if not self.staff:
            print("No staff members found.")
            return
        
        print("\n===== STAFF DIRECTORY =====")
        print(f"{'ID':<10} {'Name':<20} {'Department':<15} {'Position':<15} {'Role':<15} {'Salary':<10}")
        print("=" * 90)
        for member in self.staff:
            print(f"{member['id']:<10} {member['name']:<20} {member['department']:<15} {member['position']:<15} {member['role']:<15} {member['salary']:<10}")
            print("=" * 90)
            
    def search_staff(self, search_term):
        # Search for staff members by ID (case-insensitive)
        results = [member for member in self.staff if search_term.lower() in member['id'].lower()]
        
        if results:
            print(f"\n===== SEARCH RESULTS FOR '{search_term}' =====")
            print(f"{'ID':<10} {'Name':<20} {'Department':<15} {'Position':<15} {'Role':<15} {'Salary':<10}")
            print("=" * 90)
            for member in results:
                print(f"{member['id']:<10} {member['name']:<20} {member['department']:<15} {member['position']:<15} {member['role']:<15} {member['salary']:<10}")
        else:
            print(f"No staff members found matching '{search_term}'.")