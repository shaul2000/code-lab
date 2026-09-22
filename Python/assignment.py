#Assignment 1:
#1. Name and Last Name: Write a program that asks the user for their first name and last name separately (using two input() calls), then prints them joined together on one line. 
First_Name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")
print(f"Hello {First_Name} {Last_Name}!")

#2. Ask the user for two numbers. Print their sum. Important: Remember that input() gives text! You must convert to int ot float before adding. Example input: 5 and 10, Expected output: 15
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print(f"The sum is: {total}")

#3. Predict the output: Without running it, what will this code print?
print("5" + "5")
print(int("5") + int("5"))
print(float("5") + 5)

#Assignment 2:
# 1. Reverse & Word Count: Write a program that asks for a sentence. Print the total number of words in it.
sentence = input("Enter a sentence: ")
reversed_sentence = sentence[::-1]
word_count = len(sentence.split())
print(f"Reversed: {reversed_sentence}")
print(f"Word Count: {word_count}")

# 2. Calculator Plus: Get two numbers, modify the calculator to also calculate the remainder (%) and the power (**) of the two numbers.
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
total = first_num + second_num
diff = first_num - second_num
prod = first_num * second_num
remainder = first_num % second_num
power = first_num ** second_num
print(f"Sum: {total}")
print(f"Difference: {diff}")
print(f"Product: {prod}")
print(f"Remainder: {remainder}")
print(f"Power: {power}")

# 3. Split Challenge: Ask for a full name with middle name (e.g., "John Michael Doe"). Print the First and Last names, ignoring the middle.
full_name = input("Enter your full name (First Middle Last): ")
names_list = full_name.split()
first_name = names_list[0]
last_name = names_list[-1]
print(f"First Name: {first_name}")
print(f"Last_Name: {last_name}")

#Assignment 3:
#1. Leap Year Checker: Ask for a year. Print"Leap Year" if it's divisible by 4 (but not 100, unless also divisible by 400).

	#- Hint: Use % (modulo) and and/or.
 
year = int(input("Enter a year: "))
 
if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year!")
 
#2. Voting Eligibility: Ask for age. If age >= 18, print "You can vote". Else, print "Wait until you are 18".
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("Wait until you are 18.")

#3. Ternary Expression: Rewrite the Grade Calculator using the ternary (short) syntax: 
score = int(input("Enter your score: "))

print("Pass") if score >= 50 else print("Fail")

#Assignment 4
#1. Shopping List: Create a list of 5 items. Add one item, remove one using .remove(), then use pop() to remove the last. Print the final list.
shopping_list = ["Rice", "Beans", "Oil", "Salt", "Garri"]
print(f"Original Shopping List: {shopping_list}")

shopping_list.append("Milk")
print(f"Added item: {shopping_list}")

shopping_list.remove("Salt")
print(f"Removed salt from the list: {shopping_list}")

last_item = shopping_list.pop()
print(f"Removed last item: {last_item}")
print(f"Final Shopping List: {shopping_list}")

#2. Even Numbers: Use a list comprehension to get only the even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. #Hint - A number even if n % 2 == 0.
nums = [1, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in nums if n % 2 == 0]
print(f"Even Numbers: {even_numbers}")

#3. Class Average: Make a nested list of 3 students, each with 2 scores. Print each student's name and their total score.
students = [
    ["Samuel", 67, 89], ["Kelvin", 74, 97], ["John", 83, 39]
]
for student in students:
    name = student[0]
    total_score = student[1] + student[2]
    print(f"{name}: Total Score = {total_score}")
    
    
#Assignment 5
#1. Coordinates: Create a tuple point = (5, 10). Unpack it into x and y, then print x + y. Try changing point[0] = 3 and observe the error.
point = (5, 10)
x, y = point
print(f"Sum of x and y: {x + y}")

#2. Car Record: Build a dictionary for a car with keys: model, year, color, mileage. Print only the model and year. Then update the mileage after a trip.
rides = {
    "model": "BMW",
    "year": 2025,
    "color": "Black",
    "Mileage": 56000
}
print(f"Car: {rides["model"]} {rides["year"]}")
rides["Mileage"] = rides["Mileage"] + 500
print(f"New Mileage: {rides["Mileage"]} km")

#3. Phone Book: Create a dictionary of 3 friends and their phone numbers. Use a loop to print each friend's name and number. Then check if a specific name exists using in.
phonebook = {
    "Ultimate": "08156452678",
    "Kelvin": "09078654324",
    "Mary": "07087654543"
}
print("===== PHONE BOOK =====")
for name, number in phonebook.items():
    print(f"{name}: {number}")
    
search_name = "Kelvin"
if search_name in phonebook:
    print(f"\n✅ Found {search_name}: {phonebook[search_name]}")
else:
    print(f"\n❌ {search_name} not found in contacts.")


#Assignment 6:
#1. Even Sum: Use a for loop with range() to add up all even numbers from 1 to 50. print the total.
  #- Hint: range(2, 51, 2) gives you evens directly.
sum_total = 0
for r in range(2, 51, 2):
    sum_total += r
print(f"Sum of even numbers (1-50): {sum_total}")

#2. Countdown: Write a while loop that counts down from 10 to 1, then prints "LiftOff! 🚀".
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!🚀")

#3. Pattern Printer: Use nested loops to print this triangle:
#*
#**
#***
#****
#*****
for row in range(1, 8):
    for col in range(row):
        print("*", end="")
    print()



"""Study notes and solutions for the functions assignment."""


# 1. Concise study
#
# Keyword arguments are arguments passed by parameter name. They make a call
# easier to read, and their order does not matter.
# Example: greetings(name="Paul", age=29)
#
# Arbitrary arguments allow a function to accept an unknown number of values.
# Use *args for extra positional arguments and **kwargs for extra keyword
# arguments. Inside the function, args is a tuple and kwargs is a dictionary.
# Example: add_all(2, 4, 6) and show_details(name="Paul", age=29)
#
# A return statement sends a value back to the code that called the function.
# The returned value can be stored, printed, or used in another expression.
# A function without return sends back None.


# 2. Accept a string and return its length.
def string_length(text):
    return len(text)


# 3. Accept a character and a string and return the occurrence count.
def count_character(character, text):
    return text.count(character)


print(string_length("Python"))
print(count_character("o", "Hello, how are you?"))

