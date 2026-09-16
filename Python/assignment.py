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

