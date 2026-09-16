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




My_name = "PAUL AWAJIMIJAN"
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