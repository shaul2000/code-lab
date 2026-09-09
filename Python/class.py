def greetings(age, gender, name="There"):
    print(f"Hello {name}! Good Morning.")
    print("Welcome to my first Python function.")
    print(f"You are {age} years old {gender} gender")
    
#function invocation
greetings(29, "Male", "David")
greetings(23, "Female", "Blessing")
greetings(None, "Any")

def sum_of_numbers(a, b):
    result = a + b
    print(result)