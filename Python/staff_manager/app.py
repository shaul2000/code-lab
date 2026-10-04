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
        """Loads staff
        """