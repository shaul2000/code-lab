
📄 Project Report: Staff Management System

Author: shaul2000
Language: Python 3


1. Project Overview
The Staff Management System is a command-line interface (CLI) application designed to manage employee records securely. It serves as a foundational model for building enterprise-grade data management tools with a focus on security, data integrity, and scalable architecture.


2. Core Architecture
The system is built around a single primary class: StaffManager.

Object-Oriented Design: The class encapsulates all data and logic, promoting separation of concerns.
Data Persistence: Uses JSON for structured data storage.
Security-First: Implements defensive programming, input validation, and filesystem hardening.


3. Key Features
Features & Descriptions

ID Generation:	                                    
- Unique, sequential IDs (STF0001, STF0002) to ensure record integrity.

Audit Trails:	                                    
- Automatic tracking of "Joined Date" using UTC timestamps.

Comprehensive Search:	                            
- Allows searching across multiple fields (ID, Name, Department, Role) with case-insensitive matching.


Data Validation:	                                Validates numeric salaries and prevents empty string inputs.
CRUD Operations:	                                
- Supports full Create, Read, Update, and Delete workflows.


4. Security & Best Practices Implemented
A. Input Sanitization
All user inputs are processed using .strip() and .lower() to prevent whitespace and case-sensitivity issues. Empty inputs are rejected at the boundary.

B. Filesystem Permissions
The staff.json database is hardened using chmod 600 (Owner Read/Write only). This prevents other users on the Ubuntu system from viewing sensitive salary data.

C. Defensive Error Handling
The application uses try/except blocks to handle:

JSON Corruption: Catches JSONDecodeError without crashing.
Input Errors: Catches ValueError for invalid salary entries.
File Errors: Catches PermissionError and OSError during I/O operations.
D. DRY (Don't Repeat Yourself) Principle
Table formatting is extracted into a reusable helper method (_print_table) and class constants (HEADER, DIVIDER), ensuring the UI remains consistent and easy to maintain.


5. Technical Stack
json module: For data serialization/deserialization.
os & stat modules: For file existence checks and permission management.
datetime (UTC): For standardized, timezone-aware timestamps.
f-strings: For efficient, readable string formatting.


6. Future Enhancements (Roadmap)
Authentication: Add a login layer with salted password hashing (Layer 5).
Role-Based Access Control (RBAC): Hide salary data from non-manager users (Data Masking).
Encryption at Rest: Encrypt the staff.json file using Fernet symmetric encryption (Layer 6).
