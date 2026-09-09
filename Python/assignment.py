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

