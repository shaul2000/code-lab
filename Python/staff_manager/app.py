import json
import os
from datetime import datetime

class StaffManager:
    def __init__(self):
        self.staff = []
        self.data_file = "staff.json"
        self.next_id = 1 # Helps to generate unique IDs for new staff members
        self.load_data()    # Load existing staff data from the JSON file if it exists
        
    def load_data(self):
        """Loads staff data from the JSON file if it exists and handles missing or corrupted files."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    self.staff = json.load(file)
                    if self.staff:
                        # Update next_id to be one more than the highest existing ID
                        self.next_id = max(staff_member['id'] for staff_member in self.staff) + 1
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading data: {e}. Starting with an empty staff list.")
                self.staff = []
        else:
            print("No existing data found. Starting with an empty staff list.")