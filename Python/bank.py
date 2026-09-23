# import random package or module
import random 

# declare storage to store customer, staff and manager details
customers = []
staff_users = []
manager = {
    "username":"machinee",
    "password":"@123$456&789)"
}

# function to display the application menu
def appMenu():
    print("What do you want to perform?")
    print("1. Open/Create Account")
    print("2. Customer Login")
    print("3. Staff Login")
    print("4. Manager Login")
    print("5. Exit")

# helper to avoid crashing when user provides no input or interrupts the program
def safe_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value == "":
                print("Input cannot be empty. Please try again.")
                continue
            return value
        except (EOFError, KeyboardInterrupt):
            print("\nInput ended. Exiting the application.")
            raise SystemExit

# customers operation
# 1. account creation
# function to handle account creation
def CreateAccount():
    # collect customer data: first name, last name, phone number, email address
    # date of birth, home address, nationality, state of origin, gender
    print("\n--- Create New Account ---")
    fName = safe_input("Enter your first name: ")
    lName = safe_input("Enter your last name: ")
    phone = safe_input("Enter your phone number: ")
    email = safe_input("Enter email address: ")
    dob = safe_input("Enter your birthday(dd/mm/yyyy): ")
    home = safe_input("Enter your home address: ")
    nationality = safe_input("Enter your country: ")
    state = safe_input("Enter your state of origin: ")
    gender = safe_input("Enter your gender(M/F): ")
    
    # system auto generate account number for customer
    account = random.randint(2020000000, 2029999999)
    password = safe_input("create password: ")

#create a customer dictionary object
    new_customer = {
         "firstname": fName,
         "lastname": lName,
         "email": email,
         "phone": phone,
         "home": home,
         "gender": gender,
         "country": nationality,
         "state": state,
         "dob": dob,
         "account": account,
         "password": password,
         "balance": 0.00,
         "pin": None,
         "restricted": False
    }
    
    # store to the new customer list above
    customers.append(new_customer)
    print(f"congratulations, your account number is: {new_customer['account']}")

# function to handle user login
def login(user_type):
    loggedInUser = None
    # identify the user
    if user_type == "customer":
        # check customer login details
        email = safe_input("Enter email address: ")
        password = safe_input("Enter password: ")
        # look for the customer with the given email and password above
        for customer in customers:
            if customer["email"] == email.strip() and customer["password"] == password:
                loggedInUser = customer
                print("welcome to Customer Dashboard")
                # return the customer
                return loggedInUser
        if loggedInUser == None:
            print("incorrect login credentials")
            return loggedInUser
    elif user_type == "staff":
        staffId = safe_input("Enter your staffID: ")
        password = safe_input("Enter your password: ")
        # look through staff_users list above
        for staff in staff_users:
            if staff["id"] == staffId and staff["password"] == password:
                loggedInUser = staff
                print("welcome to staff Dashboard")
                return loggedInUser
        if loggedInUser == None:
            print("Incorrect login credentials")
            return loggedInUser
    else:
        username = safe_input("Enter username: ")
        password = safe_input("Enter password: ")
        # check if the username and password given above matches the manager detail
        if manager["username"] == username and manager["password"] == password:
            loggedInUser = manager
            print("welcome to Bank Manager Dashboard")
            return loggedInUser
        else:
            print("incorrect login credentials")
            return loggedInUser

# function to handle withdrawal
def withdrawal(customer):
    # request amount to bw withdrawn
    try:
        amount = float(safe_input("Enter amount to be withdrawn: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return customer
    # check to be sure the amount is not negative
    if amount < 0:
        print("Negative withdrawal is not allowed!")
        return customer
    # check customer's account balance if the amount to be withdrawn is available in the balance
    elif customer["balance"] >= amount:
        # debit the customer's balance
        customer["balance"] -= amount
        print("Withdrawal successful")
        print(f"Your new balance is: {customer['balance']}.")
        return customer
    else:
        print("Insufficient funds, kindly make a deposit.")
        return customer

# function to handle deposit
def deposit(customer):
    try:
        amount = float(safe_input("enter amount to be deposited: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return customer
    if amount < 0:
        print("Negative amount is not allowed")
        return customer
    else:
        # credit the amount to customer balance
        customer["balance"] += amount
        print("Deposit successful.")
        print(f"Your new balance is: {customer['balance']:.2f}")
        return customer

# function to check current customer balance
def checkBalance(customer):
    print(f"Your current balance is: {customer['balance']:.2f}")
    return customer['balance']

# function to handle transfer operation 
def transfer(sender):
    try:
        receiver_account = int(safe_input("Enter receiver account number: "))
        amount = float(safe_input("Enter amount you want to transfer: "))
    except ValueError:
        print("Invalid account number or amount entered. Please try again.")
        return None
    notFound = True
    # look through the customer list
    for customer_user in customers:
        if customer_user["account"] == receiver_account:
            customer_user["balance"] += amount
            # reduce the sender balance
            sender["balance"] -= amount
            print("Transaction successful.")
            print(f"Your new balance is: {sender['balance']}")
            notFound = False
            return None
    if notFound:
        print(f"This account number: {receiver_account} is incorrect.")

# function to handle customer's account management
def accountManagement(action):
    try:
        account = int(safe_input(f"Enter customer's account number to {action}: "))
    except ValueError:
        print("Invalid account number. Please enter a valid number.")
        return None
    notFound = True
    # loop through the the customers list to get the customer with given account number
    for customer_user in customers:
        if customer_user["account"] == account:
            if action == "restrict":
                customer_user["restricted"] = True
                print(f'{customer_user["firstname"]} account has been {action}ed.')
            elif action == "unrestrict":
                customer_user["restricted"] = False
                print(f'{customer_user["firstname"]} account has been {action}ed.')
            notFound = False
            break
    if notFound:
        print("Incorrect account number entered please try again!")

# function to add new staff user to the system by bank manager
def addStaff():
    print("==== Adding New Staff User ====")
    username = safe_input("Enter staff name: ")
    password = safe_input("Set up a secure password for the new staff: ")
    # system auto generate staffId
    staffId = f"HTI{random.randint(100000, 999999)}"
    # create a new staff dict object
    new_staff = {
        "username": username,
        "id": staffId,
        "password": password
    }
    # add new staff to the user list above using list.append() method
    staff_users.append(new_staff)
    print("New staff has been added.")
    print("==== Staff Login details ====")
    print(f"Staff ID: {new_staff['id']} password: {new_staff['password']}")

# function to delete staff
def deleteStaff():
    staffId = safe_input("Enter the staff ID to be deleted: ")
    notFound = True
    for staff in staff_users:
        if staff["id"] == staffId:
            # remove the staff
            staff_users.remove(staff)
            print("One staff has been removed from the system")
            notFound = False
            break
    if notFound:
        print("Incorrect staff ID entered. please try again!")

# function to preview all customers
def previewCustomers():
    if len(customers) <= 0:
        print("No customer record")
        return None
    for customer_user in customers:
        print(f"* {customer_user['firstname']} {customer_user['lastname']} -- {customer_user['account']} -- {customer_user['balance']}")

# main function to start the application
def startApp():
    print("welcome to HTI Banking system")
    print("===============================")
    while True:
        print("What do you want to perform?")
        print("1. Open/Create Account")
        print("2. Customer Login")
        print("3. Staff Login")
        print("4. Manager Login")
        print("5. Exit")

        try:
            main_choice = safe_input("Enter a number between 1 and 5: ")
        except SystemExit:
            break

        # determine the user inputted number
        if main_choice == "1":
            # invoke the create account function
            CreateAccount()
        elif main_choice == "2":
            # invoke the login function for customer
            loggedUser = login("customer")
            # check to see if the login function did not return None
            if loggedUser != None:
                # show the customer's dashboard menu
                print("==== WELCOME TO CUSTOMER'S DASHBOARD ====")
                while True:
                    print("What do you want to perform?")
                    print("a. Withdraw")
                    print("b. Transfer")
                    print("c. deposit")
                    print("d. Check Balance")
                    print("e. Logout")
                    try:
                        sub_choice = safe_input("Enter a character letter between a and e: ")
                    except SystemExit:
                        break
                    if sub_choice.lower() == "a":
                        # invoke the withdrawal function
                        withdrawal(customer = loggedUser)
                    elif sub_choice.lower() == "b":
                        # invoke the transfer function
                        transfer(sender = loggedUser)
                    elif sub_choice.lower() == "c":
                        # invoke the deposit function
                        deposit(customer = loggedUser)
                    elif sub_choice.lower() == "d":
                        # display the logged-in user's balance
                        checkBalance(loggedUser)
                    elif sub_choice.lower() == "e":
                        print("You are logged out.")
                        break
                    else:
                        print("Incorrect character entered. input must either be a/b/c/d/e")
                        print("please try again.")

        elif main_choice == "3":
            # invoke login function for staff
            loggedUser = login("staff")
            if loggedUser != None:
                print("==== Welcome to Staff Dashboard ====")
                while True:
                    print("What do yu want to perform?")
                    print("a. Restrict Customer's Account")
                    print("b. Un-restrict Customer's Account")
                    print("c. View All Customers")
                    print("d. Logout")
                    try:
                        sub_choice = safe_input("Enter character between a and d: ")
                    except SystemExit:
                        break
                    if sub_choice.lower() == "a":
                        # invoke the account management function to restrict
                        accountManagement(action = "restrict")
                    elif sub_choice.lower() == "b":
                        accountManagement(action = "unrestrict")
                    elif sub_choice.lower() == "c":
                        # invoke the preview customers function
                        previewCustomers()
                    elif sub_choice.lower() == "d":
                        print("You are logged out")
                        break
                    else:
                        print("Incorrect character entered. input must either be a/b/c/d")
                        print("please try again.")

        elif main_choice == "4":
            # invoke the login function for the manager
            loggedUser = login("manager")
            if loggedUser != None:
                print("=== WELCOME TO MANAGER'S DASHBOARD ===")
                while True:
                    print("What do you want to perform?")
                    print("a. Add New Staff")
                    print("b. View All Customers")
                    print("c. Remove/Delete Staff")
                    print("d. Logout")
                    try:
                        sub_choice = safe_input("Enter a character between a and d: ")
                    except SystemExit:
                        break
                    if sub_choice.lower() == "a":
                        addStaff()
                    elif sub_choice.lower() == "b":
                        previewCustomers()
                    elif sub_choice.lower() == "c":
                        deleteStaff()
                    elif sub_choice.lower() == "d":
                        print("You are logged out")
                        break
                    else:
                        print("Incorrect character entered. input must either be a/b/c/d")
                        print("please try again.")

        elif main_choice == "5":
            # exit the application
            print("You are exiting the application")
            ex = safe_input("Enter 1 to exit or 0 to cancel(1/0): ")
            if ex == "1":
                print("==== Goodbye ====")
                break
            else:
                print("welcome Back!")
                
        else:
            print("Incorrect input. Number must be between 1 and 5\nTry again.")

# start the banking application
startApp()