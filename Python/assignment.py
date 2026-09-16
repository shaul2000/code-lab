First_Name = input("First Name: ")
Last_Name = input("Last Name: ")

print("Hello, ", First_Name, " ", Last_Name, "!")

User_age = input("How old are you? ")
User_age_int = int(User_age)
Next_year_age = User_age_int + 1
print("Next year, you will be ", Next_year_age, " years old.")

print("5" + "5")
print(int("5") + int("5"))
print(float("5") + 5)

#Assignment:
# 1. Reverse & Count: Write a program that asks for a word. Print the reversed word and how many vowels (a, e, i, o, u) it has.
# 2. Calculator Plus: Modify the calculator to also calculate the remainder (%) and the power (**) of the two numbers.
# 3. Split Challenge: Ask for a full name with middle name (e.g., "John Michael Doe"). Print the First and Last names, ignoring the middle.



#Assignment:
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
    


#3. Ternary Expression: Rewrite the Grade Calculator using the ternary (short) syntax: 



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

