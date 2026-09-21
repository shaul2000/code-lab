#The Sentence Analyzer:
sentence = input("Enter a sentence: ")
reversed_sentence = sentence[::-1]
uppercase_sentence = sentence.upper()
word_count = len(sentence.split())

print(f"Original sentence: {sentence}")
print(f"Reversed sentence: {reversed_sentence}")
print(f"Uppercase sentence: {uppercase_sentence}")
print(f"Word count: {word_count}")

#Simple Calculator:
#Task: Ask for two numbers and print their sum, difference, and product.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")

#Name Splitter:
#Task: Ask for a full name and print the first and last name separately.
full_name = input("Enter your full name (First Last): ")
names = full_name.split()
first_name = names[0]
last_name = names[-1] #gets the last item in the list, which is the last name
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Hello, {first_name} {last_name}!")

#Check if a number is positive, negative, or zero.
num = int(input('Enter a number: '))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
    
#Simple Login System: Check username and password.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful!")
else:
    print("Access Denied.")
#Note: We used and because both conditions must be true to login. 


#Grade Calculator: Print "Pass" or "Fail" based on a score: (Pass = 50+).
score = int(input("Enter your score: "))

if score >= 50:
    print("Pass")
else:
    print("Fail")
    
    
nums = [10, 20, 30, 40]

a = nums.pop(0)
b = nums.pop(0)

print(a)
print(b)
print(nums) 

#Subject Manager: Create a list of subjects, add/remove items, and sort them.
subjects = ["Math", "Python", "Physics", "Chemistry"]
subjects.append("Biology")
subjects.remove("Physics")
subjects.sort()
fav_subject = subjects.pop()

print(f"My subjects: {subjects}")
print(fav_subject)
print(f"Total Courses: {len(subjects)}")

#Filter Scores (List Comprehension): Filter Scores above 60.
scores = [45, 72, 38, 88, 55, 91, 60]
passed = [s for s in scores if s > 60]
scores.sort()
best_score = scores.pop()
print(f" Passed students: {passed}")
print(f"Number who passed: {len(passed)}")
print(f"Scores {scores}")
print(f"Best Score: {best_score}")

#Student Report Card (Nested List): Build nested records and print a formatted report.
students = [
    ["Ultimate", 87, 93, 76],
    ["Mercy", 48, 89, 68],
    ["Daniel", 65, 70, 30]
]
print("===== STUDENT REPORT =====")

for student in students:
    name = student[0]
    average = (student[1] + student[2] + student[3]) / 3
    if average >= 50:
        status = "PASS"
    else:
        status = "FAIL"
    print(f"{name}: Average = {average:.2f} {status}") #Note: {average:.2f} inside an f-string means "show only 2 decimal places".
    
#Birth Date Tuple: Create a tuple for your birth date and unpack it.
birth_date = (2005, 5, 16) #year, month, day
year, month, day = birth_date
print(f"I was born on the {day}th of May({month}), {year}")
    
#Product Dictionary: Build a product record and update it.
products = {
    "name": "Wireless Mouse",
    "price": 4500,
    "category": "Accessories",
    "in_stock": True  
} 
print(f"Products: {products["name"]} - ₦{products["price"]}")
#price discount update
products["price"] = 3800
print(f"New Price: ₦{products["price"]}")
#Check stock
if products["in_stock"]:
    print("Available for purchase!")
else:
    print("Out of stock.")


#Payroll Report (Iterating a dictionary):
employees = {
    "Kelvin": 25000000,
    "Samuel": 67600000,
    "Destiny": 12300000
}
print(f"===== PAYROLL REPORT =====")
total_payroll = 0
for name, salary in employees.items():
    total_payroll += salary
    print(f"{name}: ₦{salary:,}") #{salary:,}: adds commas to big numbers
print(f"Total Payroll: ₦{total_payroll:,}") 

#10 Times Table: Print the 10-times table using a for loop.
number = 10
print(f"===== {number} TIMES TABLE =====")
for k in range(1, 13):
    result = number * k
    print(f"{number} x {k} = {result}")
    
#Password Checker: Keep asking until the correct password is entered.
correct_password = "Machinee-X"
while True:
    guess = input("Enter Password: ")
    if guess == correct_password:
        print("✅ Access Granted!")
        break
    else:
        print("❌ Wrong password. Try again.")
#Why while True? We don't know how many tries the user needs. We loop indefinitely and use break when they finally get it right. Perfect pattern for login systems! 

#Number Guessing Game: Guess a secret number with Higher?Lower hints.
import random
secret = random.randint(1, 40)
attempts = 0
print("I'm thinking of a number between 1 and 40...")

while True:
    trial = int(input("Your guess: "))
    attempts += 1
    
    if trial < secret:
        print("📈 Higher!")
    elif trial > secret:
        print("📉 Lower!")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts.")
        break
    



My_name = "Emmanuel Solomon"
My_school_name = "Federal University of Technology, Minna"

def my_second_function():
    print(My_name)
    print(My_school_name)
    
#function invocation
my_second_function()


#Function that will accept 2 numbers and find their product
def find_product(num1, num2):
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
    
    
find_product(12, 14)
find_product(18, 53)
    
 #Finding the quotient of 2 numbers
def findQ(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        quotient = num1 / num2
        print(f"The quotient of {num1} and {num2} is {quotient}")
findQ(27, 3)
findQ(27, 0)