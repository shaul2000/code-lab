# Staff Management System — My Project Report

## 1. Introduction

I built the **Staff Management System**, which I call `StaffManager`, as a Python command-line application for managing staff records. I can use it to add, view, search, update, and delete records. The application stores its data in a JSON file, validates user input, and sets restrictive file permissions to help protect the data.

I chose this project to practice the fundamentals of building a useful application while learning how to think about security from the start. It also gives me a foundation I can build on when I move the project to the web.

### What I wanted to learn

- **Software development:** object-oriented programming, file handling, error handling, and input validation.
- **Security:** file-permission hardening, input sanitization, and limiting updates to approved fields.
- **Web development:** how to structure reusable CRUD logic that I can later connect to a web interface.

### Technology I used

| Component | What I used |
|---|---|
| Programming language | Python 3 |
| Dependencies | Python standard library |
| Data storage | JSON |
| User interface | Command line with `input()` and `print()` |
| File protection | Linux file permissions (`chmod 600`) |

## 2. What I Have Built So Far

So far, I have focused on the staff-record operations and saving data locally in JSON. The current version includes creating, listing, searching, updating, and deleting records, along with input validation and file-permission hardening.

Authentication and role-based access are **not implemented yet**. I have listed them as the next stage so that the report is clear about what works today and what I still plan to build.

| Status | What it means for my project |
|---|---|
| Implemented | Staff CRUD operations, input validation, JSON persistence, file-permission hardening, whitelisted updates, and confirmed deletion |
| Planned — Layer 5 | Authentication, role-based access, and first-run administrator setup |
| Planned — Layer 6 | Encryption at rest for sensitive data |
| Longer-term goal | A web frontend and API that use my existing staff-management logic |

## 3. How I Organized the Code

I organized the application around a `StaffManager` class. The class keeps the staff records in memory and brings together the methods for saving, displaying, and managing them.

```text
StaffManager
├── Attributes
│   ├── staff: list[dict]              # Staff records held in memory
│   ├── data_file: str                 # Path to the JSON data file
│   ├── next_id: int                   # Counter for generating staff IDs
│   └── UPDATABLE_FIELDS: tuple        # Fields that an update is allowed to change
├── Persistence
│   ├── load_data()                    # Read and validate the JSON data
│   └── save_data()                    # Save the data and set file permissions
├── Display
│   └── _print_table(members)          # Display records in a formatted table
├── CRUD operations
│   ├── add_staff(...)                 # Add a staff record
│   ├── list_staff()                   # Display all staff records
│   ├── search_staff(term)             # Find matching staff records
│   ├── update_staff(staff_id)         # Update approved fields
│   └── delete_staff(staff_id)         # Delete a record after confirmation
├── Helpers
│   └── _find_member(staff_id)         # Find a record by staff ID
└── Entry point
    └── main()                         # Run the command-line menu
```

### What a Staff Record Looks Like

Each staff member is stored as a dictionary. The application generates the ID automatically and pads it with zeros. I use the ISO 8601 date format for the example joining date.

```python
{
    "id": "STF0001",
    "first_name": "Ada",
    "last_name": "Lovelace",
    "department": "Engineering",
    "position": "Developer",
    "role": "admin",
    "salary": 75000.0,
    "joined_date": "2026-10-01"
}
```

### How I Store the Data

I store the staff records in a `staff` list and keep `next_id` alongside it. That counter helps the application generate the next staff ID when a new record is added.

```json
{
    "staff": [
        { "...": "staff record" }
    ],
    "next_id": 3
}
```

## 4. Features

### Features I Have Implemented — Layers 1–4

| Layer | What I implemented | Why it matters |
|---|---|---|
| 1 | Creating, reading, and searching records | I normalize text with `.strip()` and `.lower()` where appropriate, so extra spaces and letter case are less likely to affect a search. |
| 2 | Input validation | I check that required text is not empty and that salary is a non-negative number. |
| 3 | File-permission hardening | I use `chmod 600` to limit the data file to owner read/write access on supported Linux systems. |
| 4 | Updating and deleting records | I only allow updates to whitelisted fields, and I ask for confirmation before deleting a record. The default answer is no. |

### Features I Plan to Add — Layer 5

| Feature | Why I want to add it |
|---|---|
| Authentication with salted password hashing | I do not want to store passwords as plain text. |
| Role-based access control | I want to limit administrative operations to the right users. |
| First-run setup | I want the application to guide me through creating the first administrator account. |

## 5. Security: What I Have Done and What I Still Need to Do

Security is one of the areas I am trying to consider as I build the project. The safeguards below are part of the current implementation; the login-related items are future improvements.

### Safeguards in the Current Version

- **File permissions:** I set the data file to owner read/write permissions (`600`) during the save and successful load paths. This helps prevent other local users from reading staff details, including salaries.
- **Input normalization:** I strip surrounding whitespace from text input and use case-insensitive comparisons for searches and staff ID lookups where appropriate.
- **Whitelisted updates:** I use `UPDATABLE_FIELDS` to specify which fields can be edited. This helps prevent a general update operation from changing protected fields, such as a user's role. If I add fields such as `password_hash` or `salt`, I will keep them out of the whitelist unless there is a specific reason to allow edits.
- **Safer failure behavior:** An empty file is treated as an empty staff list. If the JSON is corrupted, the application displays an error instead of crashing without explanation. For deletion, the `[y/N]` prompt makes “no” the default.
- **Error handling:** I handle expected JSON, permission, operating-system, and value errors so that users do not see raw stack traces for these cases.
- **In-place updates:** `_find_member()` returns the actual staff dictionary held in memory. That lets an update change the stored record directly without making an unnecessary copy.

### Improvements I Have Planned

| Issue I still need to address | Severity | My planned direction |
|---|---|---|
| Salary values are stored as plain text in JSON | Medium | I plan to investigate encryption at rest in Layer 6. |
| The application does not have authentication yet | High | I plan to add a login flow and salted password hashing in Layer 5. |
| A future login could reveal too much through its error messages | Medium | I plan to use a generic response, such as “Invalid ID or password.” |
| A future login could be repeatedly guessed | Medium | I plan to consider tracking failed attempts and applying a lockout policy. |

The last three items are considerations for the login feature I plan to add; the current version does not have a login system.

## 6. Code Quality and Project Size

I have tried to keep the code understandable by giving methods clear responsibilities and reusing helpers where they make sense.

| Area | How I approached it |
|---|---|
| Avoiding repetition | I share `_find_member()` between update and delete operations, reuse `_print_table()`, and keep the update whitelist in `UPDATABLE_FIELDS`. |
| Method responsibilities | I use separate methods for tasks such as loading data, saving data, adding records, and displaying records. |
| Validation | I return early when validation fails, which helps keep the code from becoming deeply nested. |
| Testability | My methods accept arguments, so I can test their behavior without relying entirely on interactive input. |
| Documentation | I have added docstrings to public methods and comments where they help explain a decision. |
| Naming | I use descriptive names such as `first_name`, `staff_id`, and `UPDATABLE_FIELDS` to make the code easier to follow. |

### Approximate Project Size

- `app.py` is approximately 230 lines.
- The size of `staff.json` depends on how many staff records I add. The records are written with four-space indentation.

## 7. Current Limitations

There are still some things the application does not handle. I have noted these so I can use them to guide future improvements:

- **Concurrent access:** I store the data in one JSON file and have not added a locking mechanism for simultaneous access.
- **Search options:** I search text fields but have not added searches by salary or rank.
- **Interface:** The project currently runs in the command line. I have not built the web interface yet.
- **Backups:** `staff.json` is currently the single source of truth, and I have not added backup or restore features.
- **Large lists:** `list_staff()` prints every record, so pagination may be useful if the dataset grows.
- **Authentication and authorization:** I have not added these yet; they are part of my Layer 5 plan.

## 8. What I Plan to Do Next

### Layer 5 — Authentication and Access Control

My next major step is to add authentication and decide how access should depend on a user's role. I plan to:

1. Store password hashes and salts rather than plaintext passwords.
2. Require users to log in before they can reach the menu.
3. Restrict CRUD operations according to the user's role, with administrative operations available only to administrators where appropriate.
4. Guide the user through creating the initial administrator account during first-run setup.
5. Use generic login errors and consider how to handle repeated failed attempts.

### Layer 6 — Protecting Sensitive Data at Rest

After that, I plan to look at protecting sensitive stored information, especially salary values. I will:

1. Evaluate encryption for sensitive fields such as salary.
2. Consider a vetted library such as `cryptography.fernet`.
3. Keep any encryption key outside the repository and plan how the application will obtain it securely.

Password hashes should remain protected with a purpose-built password-hashing algorithm; they should not be treated as data that needs reversible encryption.

### Longer-Term Goal — A Web Frontend and API

Once the core behavior is ready, I would like to expose it through a framework such as Flask or FastAPI and build an HTML/CSS/Bootstrap frontend. The API could provide routes like these:

| HTTP method and route | What I expect it to do |
|---|---|
| `POST /api/staff` | Add a staff record |
| `GET /api/staff` | List or search staff records |
| `PATCH /api/staff/<id>` | Update a staff record |
| `DELETE /api/staff/<id>` | Delete a staff record |

## 9. What I Have Gained from the Project

This project has helped me practice several areas of development at the same time:

- **Software engineering:** I have worked with object-oriented design, CRUD operations, validation, file handling, and error handling.
- **Security:** I have applied file-permission hardening, input normalization, and update whitelisting, and I have a plan for adding authentication.
- **Web development foundations:** I am building reusable management logic that I can later connect to an API and a web application.

Overall, I see `StaffManager` as both a working command-line project and a base I can keep improving as I learn more about application development and security.
