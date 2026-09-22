# import random package or module
import random 

# declare storage to store customer, staff and manager details

customers = []
staff_users = []
manager = {
    "username":"manager",
    "password":"12345678"
}
# function to display the application menu

def appMenu():
    print("What do you want to perform?")
    print("1. Open/Create Account")
    print("2. Customer Login")
    print("3. Staff Login")
    print("4. Manager Login")
    print("5. Exit")

# customers operation
# 1. account creation
# function to handle account creation

def CreateAccount():
    # collect customer data: first name, last name, phone number, email address
    # date of birth, home address, nationality, state of origin, gender
    fName = input("Enter your first name: ")
    lName = input("Enter your last name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter email address: ")
    dob = input("Enter your birthday(dd/mm/yyyy): ")
    home = input("Enter your home address: ")
    nationality = input("Enter your country: ")
    state = input("Enter your state of origin: ")
    gender = input("Enter your gender(M/F): ")
    # system auto generate account number for customer
    account = random.randint(2020000000, 2029999999)
    password = input("create password")

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
    print(f"congratulations, your account number is: {new_customer["account"]}")

# function to handle user login

def login(user):
    logggedInUser = None
    # identify the user
    if user == "customer":
        # check customer login details
        email = input("Enter email address: ")
        password = input("Enter password: ")
        # look for the customer with the given email and password above
        for customer in customers:
            if customer["email"] == email.strip() and customer["password"] == password:
                logggedInUser = customer
                print("welcome to Customer Dashboard")
                # return the customer
                return logggedInUser
        if logggedInUser == None:
            print("incorrect login credentials")
            return logggedInUser
    elif user == "staff":
        staffId = input("Enter your staffID: ")
        password = input("Enter your password: ")
        # look through staff_users list above
        for staff in staff_users:
            if staff["id"] == staffId and staff["password"] == password:
                logggedInUser = staff
                print("welcome to staff Dashboard")
                return logggedInUser
        if logggedInUser == None:
            print("Incorrect login credentials")
            return logggedInUser
    else:
        username = input("Enter username: ")
        password = input("Enter password: ")
        # check if the username and password given above matches the manager detail
        if manager["username"] == username and manager["password"] == password:
            logggedInUser = manager
            print("welcome to Bank Manager Dashboard")
            return logggedInUser
        else:
            print("incorrect login credentials")
            return logggedInUser

# functtion to handle withdrawal
def withdrawal(customer):
    # request amount to bw withdrawn
    amount = float(input("Enter amount to be withdrawn"))
    # check to be sure the amount is not negative
    if amount < 0:
        print("Negative withdrawal is not allowed!")
        return customer
    # check customer's account balance if the amount to be withdrawn is available in the balance
    elif customer["balance"] > amount:
    # debit the customer's balance
         customer["balance"] -= amount
         print("withdrawal succesful")
         print(f"your new balance is: {customer["balance"]}.")
         return customer
    else:
        print("insufficient funds, kindly make a deposit.")
        return customer

# function to handle deposit
def deposit(customer):
    amount = float(input("enter amount to be deposited: "))
    if amount < 0:
        print("Negative amount is not allowed")
        return customer
    else:
        # credit the amount to customer balance
        customer["balance"] += amount
        print("Deposit successful.")
        print(f"Your new balance is: {customer["balance"]}")
        return customer

# function to handle transfer operation 
def transfer(sender):
    receiver_account = int(input("Enter receiver account number: "))
    amount = float(input("Enter amount you want to transfer: "))
    notFound = True
    # look through the customer list
    for customer_user in customers:
        if customer_user["account"] == receiver_account:
            customer_user["balance"] += amount
            # reduce the sender balance
            sender["balance"] -= amount
            print("Transaction successful.")
            print(f"Your new balance is :{sender["balance"]}")
            notFound = False
            return None
    if notFound:
        print(f"This account number: {receiver_account} is incorrect.")

# function to handle customer's account management

def accountManagement(action):
    account = int(input(f"Enter customer's account number to {action}"))
    notFound = True
    # loop through the the customers list to get the customer with given account number
    for customer_user in customers:
        if customer_user["account"] == account:
            if action == "restrict":
                customer_user["restricted"] = True
                print(f"{customer_user["firstname"]} account has been {action}ed.")
            elif action == "unrestrict":
                customer_user["restricted"] = False
                print(f"{customer_user["firstname"]} account has been {action}ed.")
        notFound = False
    if notFound:
        print("Incorrect account number entered please try again!")

# function to add new staff user to the system by bank manager
def addStaff():
    print("==== Adding New Staff User ====")
    username = input("Enter staff name: ")
    password = input("Set up a secure password for the new staff: ")
        # system auto generate staffId
    staffId = f"HTI{random.randint(100000, 999999)}"
    # create a new staff dict object
    new_staff = {
        "username":username,
        "id":staffId,
        "password":password
    }
    # add new staff to theuser list above using list.append() method
    staff_users.append(new_staff)
    print("New staff has been added.")
    print("==== Staff Login details ====")
    print(f"Staff ID: {new_staff["id"]} password: {new_staff["password"]}")

# function to delete staff
def deleteStaff():
    staffId = input("Enter the staff ID to be deleted: ")
    notFound = True
    for staff in staff_users:
        if staff["Id"] == staffId:
            # remove the staff
            staff_users.remove(staff)
            print("one staff has been removed from the system")
            notFound = True
            break
    if notFound:
        print("Incorrect staff ID entered. please try again!")

# function to preview all customers
def previewCustomers():
    if len(customers) <= 0:
        print("No customer record")
        return None
    for customer_user in customers:
        print(f"* {customer_user["firstname"]} {customer_user["lastname"]} -- {customer_user["account"]} -- {customer_user["balance"]}")

# main function to start the application
def startApp():
    print("welcome to HTI Banking system")
    print("===============================")
    while True:
        print("what do you want to perform?")
        main_choice = input("Enter a number between 1 and 5: ")
        # determine the user inputted number
        if main_choice == "1":
            # invoke the create account function
            CreateAccount()
        elif main_choice == "2":
            # invoke the login function for customer
            loggedUser = login(user = "customer")
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
                    sub_choice = input("Enter a character letter between a and e: ")
                    if sub_choice.lower() == "a":
                        # invoke the withdrawal function
                        withdrawal(customer = loggedUser)
                    elif sub_choice.lower() == "b":
                        # invoke the transfer function
                        transfer(sender = loggedUser)
                    elif sub_choice.lower() == "c":
                        # invoke the deposit fuction
                        deposit(customer = loggedUser)
                    elif sub_choice.lower() == "d":
                        # display the user balance
                        print(f"Your current balance is: {loggedUser["balance"]}")
                    elif sub_choice.lower() == "e":
                        print("You are logged out.")
                        break
                    else:
                        print("Incorrect character entered. input must either be a/b/c/d/e")
                        print("please try again.")

        elif main_choice == "3":
            # invoke login function for staff
            loggedUser = login(user = "staff")
            if loggedUser != None:
                print("==== Welcome to Staff Dashboard ====")
                while True:
                    print("What do yu want to perform?")
                    print("a. Restrict Customer's Account")
                    print("b. Un-restrict Customer's Account")
                    print("c. View All Customers")
                    print("d. Logout")
                    sub_choice = input("Enter character between a and d: ")
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
            login(user = "manager")

        elif main_choice == "5":
            # exit the application
            print("You are exiting the application")
            ex = input("Enter 1 to exit or 0 to cancel(1/0): ")
            if ex == "1":
                print("==== Goodbye ====")
                break
            else:
                print("welcome Back!")
                
        else:
            print("Incorrect inout. Number must be between 1 and 5\nTry again.")