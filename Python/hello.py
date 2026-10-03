print("Hello World") # Prints a basic greeting to the screen
print(5 + 5) # Adds two numbers and prints the result: 10

name = "Kelvin" # str = text (must be in quotes)
age = 24 # int = whole number
gpa = 3.5 # float = decimal number
is_student = True # bool = true or false

print("My name is " + name) # Combines text and a variable into one message
print("I am " + str(age) + " years old") # Converts age to text before joining it with the sentence
print("My GPA is " + str(gpa)) # Converts the float to text before printing it
print("I am a student: " + str(is_student)) # Converts the boolean to text so it can be printed

print(type(age)) # Shows the data type of age (it should be <class 'int'>)

x = "10" # This is a string, not an integer.
Y = int(x) # This converts the string to an integer.
print(type(Y)) # Shows that Y is now an integer after conversion
print(type(x)) # Shows that x is still a string
print( x + x) # Concatenates the string twice, so "10" + "10" becomes "1010"
print( Y + Y) # Adds the integer values, so 10 + 10 = 20
print(Y + 30) # Adds 30 to the integer value of Y, giving 40

name = input("What is your name? ") # This asks the user for input.
age = input("What is your age? ") # This asks the user for input.
print("Hello " + name + ", you are " + age + " years old.") # Prints a greeting using the user's input
# input() always returns a string, so you must convert it to int before doing math
# This is why age is kept as text here instead of being added to a number

input("Press enter to exit") # Pauses the program until the user presses Enter


name = "Kelvin"
height = 1.75 # float = decimal number
gpa = 3.5 # float = decimal number
is_student = True # bool = true or false

print("Name:", name) # Prints the person's name with a label
print("Height:", height) # Prints the height value with a label
print("GPA:", gpa) # Prints the GPA with a label
print("Is student:", is_student) # Prints the boolean value with a label

age_str = "24" # string
age_int = int(age_str) # Convert the string to an integer.

next_year = age_int + 1 #add 1 to the integer value of age
print("Next year, I will be", next_year, "years old.") # Displays the person's next age after adding 1

print(name.upper()) # Converts the name to uppercase letters
print(name.lower()) # Converts the name to lowercase letters

sentence = "Python is a great programming language."
words = sentence.split() # Splits the sentence into a list of words
print(words) # Shows the full list of words
print(words[0]) # Prints the first word in the sentence
print(words[-1]) # Prints the last word in the sentence


text = "Hello, Good morning, how are you?"
new_text = text.replace("morning", "afternoon") # Replace "morning" with "afternoon".
print(new_text) # Prints the sentence after replacing the word "morning" with "afternoon"
count = text.count("o") # Counts how many times the letter "o" appears in the text
print("The letter 'o' appears", count, "times in the text.") # Shows the final count


word = "Information"
print(word[0]) # Prints the first character: I
print(word[6]) # Prints the seventh character: a
print(word[-1]) # Prints the last character: n
print(word[0:3]) # Prints the first three characters: Inf
print(word[3:6]) # Prints characters 4 to 6: orm
print(word[6:]) # Prints from the seventh character onward: ation
print(word[:6]) # Prints the first six characters: Inform
print(word[::2]) # Prints every second character: Ifrain
print(word[::-1]) # Prints the word backwards: noitamrofnI


name = "Kelvin"
age = 24

# Old way (harder to read because of string joining)
print("My name is " + name + " and I am " + str(age)) # Joins text and variables using + and str()

# New way (f-string) - cleaner and easier to read
print(f"My name is {name} and I am {age}") # Inserts values directly inside the string


print(5 == 5) # Checks whether 5 is equal to 5 -> True
print(5 != 5) # Checks whether 5 is not equal to 5 -> False
print(5 != 3) # Checks whether 5 is not equal to 3 -> True
print(5 > 3) # Checks whether 5 is greater than 3 -> True
print(5 < 3) # Checks whether 5 is less than 3 -> False
print(3 > 5) # Checks whether 3 is greater than 5 -> False
print(3 < 5) # Checks whether 3 is less than 5 -> True
print(5 >= 5) # Checks whether 5 is greater than or equal to 5 -> True
print(5 <= 5) # Checks whether 5 is less than or equal to 5 -> True
print(3 <= 5) # Checks whether 3 is less than or equal to 5 -> True
print(3 >= 5) # Checks whether 3 is greater than or equal to 5 -> False
print(5 <= 3) # Checks whether 5 is less than or equal to 3 -> False

score = 85
if score >= 90: # If the score is 90 or more, print an A
    print("Grade: A")
elif score >= 80: # Otherwise, if the score is 80 or more, print a B
    print("Grade: B")
else: # If neither condition is true, print a lower grade
    print("Grade: C or lower")
    


age = 25
has_ticket = True

if age >= 18 and has_ticket: # Both conditions must be true to allow entry
    print("You can enter!") # Both must be true
if age < 18 or has_ticket: # At least one condition must be true
    print("Special entry allowed.") # Only one needs to be true
if not has_ticket: # Reverses the boolean value
    print("You do not have a ticket.") # Reverses True to False or False to True
    

    
if 0:
    print("This won't run") # 0 is false, so this block is skipped
    
if 5:
    print("This WILL run")      # 5 is a non-zero number, so it is treated as True

if -1:
    print("This WILL also run") # -1 is also non-zero, so it is treated as True

if "hello":
    print("This runs too")      # A non-empty string is considered True

if "":
    print("Won't run")          # An empty string is considered False, so it is skipped
    
# List Examples
subjects = ["Math", "Python", "Physics"]
print(subjects) # Prints the whole list: ['Math', 'Python', 'Physics']
print(subjects[0]) # Prints the first item: "Math"
print(subjects[-1]) # Prints the last item: "Physics"
print(len(subjects)) # Prints the number of items in the list: 3

# Slicing, sorting and searching
nums = [10, 20, 30, 40, 50]
print(nums[1:4]) # Prints items from index 1 to 3: [20, 30, 40]
print(nums[::-1]) # Reverses the list: [50, 40, 30, 20, 10]

# Sorting
scores = [85, 42, 90, 67]
scores.sort() # Sorts the original list in place: [42, 67, 85, 90]
print(sorted(scores, reverse=True)) # Creates a new reversed sorted copy: [90, 85, 67, 42]
print(scores) # Shows the original list after sorting in ascending order

# Searching using 'in'
if "Python" in subjects:
    print("Python is on my timetable") # Runs only if "Python" is in the list
    
courses = ["Math", "Python", "Physics"]    
courses.append("Chemistry") # Adds Chemistry to the end of the list
fav_course = courses.pop(2) # Removes and returns the item at index 2: "Physics"
courses.remove("Math") # Removes "Math" from the list

print(courses) # Prints the updated list
print(fav_course) # Prints the removed item: "Physics"


stu_scores = [45, 72, 38, 88, 55, 91]
stu_scores.sort() # Sorts the list in ascending order
passed = [s for s in stu_scores if s > 60] # Keeps only scores greater than 60
print(passed) # Displays the passing scores

passed = []
for m in stu_scores:
    if m >= 60:
        passed.append(m) # Adds a score to the passing list if it is 60 or above
    else:
        print(f"Failed: {m}") # Prints each failed score below 60

# After the loop finishes, print the final list of passing scores
print(f"Final Passed List: {passed}") # Shows the completed pass list

students  = [
    ["David", 90, 85], ["Ada", 78, 92], ["Mark", 55, 60]
]
print(students[0]) # Prints the first student record
print(students[0][0]) # Prints the first student's name
print(students[1][2]) # Prints Ada's second score (92)

birth_date = (1999, 5, 16) # A tuple storing year, month, and day
print(f"Birth Year: {birth_date[0]}") # Show the year from the tuple

year, month, day = birth_date # Unpack the tuple into separate variables
print(f"Born on {day}/{month}/{year}") # Print the date in day/month/year format

student = { # This is a dictionary.
    "name": "Samuel",
    "age": 23,
    "gpa": 4.6
}
print(f"Student's Name: {student['name']}") # Access a value using its dictionary key
print(f"Student's Age: {student['age']}") # Print the age from the dictionary
print(f"Student's GPA: {student['gpa']}") # Print the GPA from the dictionary
# Notice: student['name'] is easier to read than student[0]
total = 0

for i in range(1, 101):     # Numbers 1 through 100
    total += i

print(f"Sum of 1 to 100: {total}")
# Output: Sum of 1 to 100: 5050
print(f"Student's Grade: {student.get('grade', 'N/A')}") # Use get() so that missing keys can return a default value

# Creating a dictionary with product details
products = {"name": "Dell Laptop", "price": "$800"} # A dictionary stores data as key-value pairs

# Accessing values using keys
print(f"Product Name: {products['name']}, Price: {products['price']}") # Shows the product's name and price

# Updating an existing value in the dictionary
products["price"] = "$750" # Changes the price to a new value
print(f"Updated Price: {products['price']}") # Prints the updated price

# Adding a new key-value pair to the dictionary
products["category"] = "Electronics" # Adds a new category field to the dictionary
print(f"Updated Product: {products}") # Prints the whole dictionary after the update

# Sorting dictionary keys alphabetically
sorted_keys = sorted(products.keys()) # Creates a sorted list of the dictionary's keys
print(f"Sorted Dictionary Keys: {sorted_keys}") # Prints the sorted keys in order

# Loop through the sorted keys and print each key-value pair
for key in sorted(products):
    print(f"{key}: {products[key]}") # Prints each key and its matching value in sorted order

# Deleting a key from the dictionary
category = products.pop("category") # Removes the category entry and stores it in the variable category
print(f"After Deletion: {products}") # Shows the dictionary after removing the key
print(f"Category: {category}") # Prints the removed value so we can see what was deleted

del products["price"] # Deletes the price key directly from the dictionary
print(products) # Shows the dictionary after removing the price entry

car = {
    "brand": "BMW",
    "year": 2025,
    "color": "Black"
}
print(f"Car Brand: {car['brand']}") # Accesses the value stored under the brand key

car["year"] = 2027 # Updates the value of an existing key
print(f"Updated Car Year: {car['year']}")

car["mileage"] = 70000 # Adds a new key-value pair to the dictionary
print(f"Car Mileage: {car['mileage']}")

del car["color"] # Removes the color key and its value.
print(f"Car Information{car}") # Shows the remaining car details.

# These methods return views of the dictionary's keys, values, and key-value pairs
print(car.keys())
print(car.values())
print(car.items())

# A nested dictionary stores another dictionary as the value of a key
ift_student = {
    "name": "Felix",
    "age": 24,
    "address": {
        "city": "Lagos",
        "state": "Lagos State"
    }
}
# Accesses the city value by following the address key into the inner dictionary
print(ift_student["address"]["city"]) # Output: Lagos

# Updates a value inside the nested address dictionary
ift_student["address"]["city"] = "Abuja"
print(ift_student["address"])

# Adds a new key-value pair to the nested address dictionary
ift_student["address"]["country"] = "Nigeria"
print(ift_student ["address"])
print(f"Student Country:{ift_student["address"] ["country"]}") # Prints the new country value.

# Each student ID maps to a dictionary containing personal details and scores
cpt_students = {
    "S001": {
        "name": "Kelvin",
        "age": 24,
        "scores": [90, 85, 78] # A list can also be stored as a dictionary value
    },
    "S002": {
        "name": "Samuel",
        "age": 22,
        "scores": [78, 93, 86]
    }
}

# Accesses Samuel's record, then the scores list, and finally its third item
print(f"{cpt_students["S002"]["scores"][2]}")


# Loop through each item in a list.
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
# Python assigns one item at a time to fruit and runs the loop body.

# Strings are sequences of characters, so a loop can visit each character.
for letter in "Python":
    print(letter)
    
# .items() provides each dictionary key and value together.
marks = {"Mary": 90, "John": 75}
for name, mark in marks.items():
    print(f"Name: {name} Mark {mark}")
    

# range(stop) starts at 0 and stops before 5.
for p in range(5):
    print(p)
    
# range(start, stop) includes 1 and stops before 6.
for q in range(1, 6):
    print(q)
    
# A step of 2 selects the even numbers from 2 through 20.
for e in range(2, 21, 2):
    print(e, end=" ")
    
# A step of 2 selects the odd numbers from 1 through 19.
for a in range(1, 20, 2):
    print(a)
    
# A negative step counts backward from 10 to 1.
for s in range(10, 0, -1):
    print(s)
print("Liftoff!  🚀")

# Print the multiples of 5 from 5 through 50.
for x in range(5, 51, 5):
    print(x, end=" ")
   
# Print the 6 times table from 1 to 40.
number = 6
for n in range(1, 41):
    print(f"{number} x {n} = {number * n}")
    
# Add each number from 1 through 200 to a running total.
total = 0
for o in range(1, 201):
    total += o
print(f"Sum of 1 to 200: {total}")

# Multiply the numbers from 1 through 20 into a running product.
# The product starts at 1 because multiplying by 0 would always produce 0.
product = 1
for m in range(1, 21):
    product *= m
print(product)

# Use an index when both the position and the item are needed.
my_fruits = ["Pineapple", "Guava", "Orange", "Watermelon"]
for index in range(len(my_fruits)):
    print(f"item {index}: {my_fruits[index]}")
    

# A while loop repeats as long as its condition remains true.
# Change the condition during each iteration to avoid an infinite loop.
count = 1 
while count <= 5:
    print(count)
    count += 1
    
    
# Stop the loop immediately when n reaches 5.
for n in range(1, 25):
    if n == 5:
        break
    print(n)
    
# Skip the number 5 and continue with the next iteration.
for x in range(1, 9):
    if x == 5:
        continue
    print (x)
    
# Use pass as a placeholder when no action is needed yet.
for u in range(8):
    pass

# A nested loop runs the inner loop completely for each outer-loop iteration.
for row in range(3):  # The outer loop runs three times.
    for col in range(3):  # The inner loop runs three times per row.
        print(f"({row}, {col})", end=" ")
    print()  # Start a new line after each row is complete.
    
# FUNCTIONS: used to group repeated code and make programs easier to manage.
# A function can take parameters, perform logic, and return a value when needed.

def greeting(name):  # name is a parameter, which acts like a placeholder.
    print(f"Hello there! {name}")  # The value passed in is displayed here.


greeting("Samuel")  # We pass the actual value "Samuel" to the function.

# RETURN VALUES: a function can send back data using the return keyword.
def add(a, b):
    return a + b  # This returns the sum of a and b.


result = add(5, 3)
print(result)  # Prints 8

# DEFAULT ARGUMENTS: optional parameters that already have a value.
def greet(person_name, greeting="Hello"):
    print(f"{greeting}, {person_name}")


greet("Machinee")  # Uses the default greeting: Hello Machinee!
greet("Ada", "Hi")  # Overrides the default with Hi.

# *args: allows a function to accept any number of positional arguments.
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 8, 10))
print(sum_all(100, 200, 300, 400, 500, 600, 700))

# **kwargs: allows a function to accept any number of keyword arguments.
def build_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


build_profile(name="Kelvin", age=24, city="Lagos")

# VARIABLE SCOPE: local variables exist only inside a function, while global variables exist outside.
count = 100  # This is a global variable.


def my_func():
    count = 5  # This is a local variable and does not change the global one.
    print(count)


my_func()  # Prints 5
print(count)  # Prints 100 because the global value was not changed.

# LAMBDA FUNCTION: a small anonymous function used for quick operations.
# Regular function example.
def square(x):
    return x ** 2


print(square(8))

# Lambda version: same idea, but written in one line.
square_lambda = lambda x: x ** 2
print(square_lambda(5))

# DOCSTRINGS: documentation text inside a function that explains what it does.
def square(x):
    """
    Returns the square of a number.

    Parameters:
    x (int or float): The number to square.

    Returns:
    int or float: The squared value of x.
    """
    return x ** 2


print(square(4))  # Prints 16


# Basic class example: a Dog object combines data (attributes) and behavior (methods).
class Dog:
    def __init__(self, name, age):
        self.name = name    #Data (attribute)
        self.age = age      #Data (attribute)
        
    def bark(self):         #Behavior (method)
        print(f"{self.name} says: Woof!")
        
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

dog1.bark()   # Rex says: Woof!
dog2.bark()   # Bella says: Woof!

my_dog = Dog("Rex", 3)    #Calls__init__automatically
print(my_dog.name)   #Rex
print(my_dog.age)   # 3

# Inheritance lets a child class reuse code from a parent class.
# This second Dog definition intentionally reuses the name for the inheritance example.
class Animal:      # Parent class (also called a base class)
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # Controls the readable text shown when an Animal object is printed.
        return f"Animal name: {self.name}"
        
    def speak(self):
        print("Some generic animal sound")  # The general version of the method
        
class Dog(Animal): # Child class - inherits from Animal
    # This method overrides Animal.speak() with a dog-specific version.
    def speak(self):
        print(f"{self.name} says: Woof!")
        
class Cat(Animal):   # Another child class with its own version of speak()
    def speak(self):
        print(f"{self.name} says: Meow!")
        
# Create objects from the child classes and call their overridden methods.
d = Dog("Rex")
c = Cat("Whiskers")

d.speak()   # Rex says: Woof!
c.speak()   # Whiskers says: Meow!

# Because __str__ is inherited, print(d) uses Animal.__str__().
print(d)     # Animal name: Rex


# Puppy inherits from Dog, so Dog is Puppy’s parent class here.
class Puppy(Dog):
    def speak(self):
        # super() calls the parent class method before adding new behavior.
        super().speak()  # Calls Dog.speak(), which prints the Woof! message.
        print(f"{self.name} is still a puppy.")


# Calling Puppy.speak() runs both the parent and child messages.
puppy = Puppy("Buddy")
puppy.speak()
print(puppy)  # Puppy also inherits the parent's __str__() method.


# Arithmetic Operators: __add__, __sub__, and other special methods.
# A Vector stores a position or direction using x and y coordinates.
class Vector:
    def __init__(self, x, y):
        # Save the coordinates on this Vector object.
        self.x = x
        self.y = y
        
    def __add__(self, other):
        # Add matching coordinates and return a new Vector with the result.
        return Vector(self.x + other.x, self.y + other.y)
    
# Create two vectors that will be added together.
v1 = Vector(1, 2)
v2 = Vector(3, 4)
# Python translates v1 + v2 into a call to v1.__add__(v2).
v3 = v1 + v2      

# Display the x and y coordinates of the resulting vector.
print(v3.x, v3.y)  # Output: 4 6


# Comparison Operators: __eq__, __lt__, etc.
# A Point represents a location that can be compared with another Point.
class Point:
    def __init__(self, x, y):
        # Store the point's coordinates for later comparison.
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        # Two points are equal when both of their coordinates match.
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        # A point is less than another when its distance from the origin is smaller.
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True, because both points have the same coordinates.
p3 = Point(0, 1)
print(p3 < p1)   # True, because p3 is closer to the origin

p4 = Point(3, 4)
print(p4 < p1)   # False, because p4 is farther from the origin

# Length: __len__
# A custom class that represents a collection of items and supports the len() function.
class MyCollection:
    def __init__(self, items):
        # Store the items in a list for later use.
        self.items = items
        
    def __len__(self):
        # Return the number of items in the collection.
        return len(self.items)

# Create an instance of MyCollection and use len() to get its length.
collection = MyCollection(["LV Bag", "Leather Belt", "Iphone 18pro", "Wristwatch", ""])
print(len(collection))  # Output: 5

# Calling an Object: __call__
# You can make an object respond to function-call syntax.
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, This is {self.name}!")

# Create an instance of Greeter and call it like a function.
greeting = Greeter("Kelvin")
greeting()  # Output: Hello, This is Kelvin!


# Encapsulation: keep an object's data protected and control access through methods.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Double underscore name-mangles the internal attribute.

    def deposit(self, amount):
        # Only allow positive amounts to be added to the account.
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        # Prevent withdrawals that are larger than the current balance.
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        # Provide controlled, read-only access to the balance.
        return self.__balance


account = BankAccount("Kelvin", 1000)
account.deposit(250)
account.withdraw(100)
print(account.owner, account.get_balance())  # Output: Kelvin 1150


# Abstraction: define the required action without specifying every implementation detail.
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        # Every payment method must provide its own version of pay().
        pass


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} by card."


class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} in cash."


# The user of these objects only needs to call pay(); each class handles the details.
payments = [CardPayment(), CashPayment()]
for payment in payments:
    print(payment.pay(50))


# Polymorphism: different classes can respond to the same method in their own way.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class RectangleShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# The same area() call works for both shapes, even though the calculations differ.
shapes = [Circle(3), RectangleShape(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area()}")


# Duck typing: an object can be used if it provides the required method,
# regardless of its class or inheritance relationship.
class EmailNotifier:
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotifier:
    def send(self, message):
        return f"SMS sent: {message}"


def notify_user(notifier, message):
    # This function only cares that notifier has a send() method.
    print(notifier.send(message))


# These unrelated classes both work because they follow the same behavior.
notify_user(EmailNotifier(), "Your order is ready.")
notify_user(SMSNotifier(), "Your order is ready.")

# FILE HANDLING
# File handling lets a program save information to a file and read it later.
# The "with" statement automatically closes the file when the indented block ends.

from pathlib import Path

file_path = Path("file_handling_demo.txt")

# 1. Writing to a file
# "w" means write. It creates the file if it does not exist,
# or replaces its contents if it already exists.
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Python file handling practice\n")
    file.write("Files can store information between program runs.\n")
    file.write("The with statement closes this file for us.\n")

print(f"Created: {file_path}")


# 2. Reading the entire file
# "r" means read. This is the default mode, but writing it explicitly is clear.
with open(file_path, "r", encoding="utf-8") as file:
    contents = file.read()

print("\n--- Entire file ---")
print(contents)


# 3. Reading one line at a time
# A for loop reads each line in order without loading all lines at once.
print("--- Reading line by line ---")
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline at the end of each line.


# 4. Appending to a file
# "a" means append. It adds new content to the end without erasing existing content.
# Include "\n" to start the new text on its own line.
with open(file_path, "a", encoding="utf-8") as file:
    file.write("This sentence was added later.\n")

print("\n--- File after appending ---")
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())


# 5. Handling a file that cannot be found
# If a file does not exist, opening it in read mode raises FileNotFoundError.
missing_file = Path("this_file_does_not_exist.txt")

try:
    with open(missing_file, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print(f"\nCould not find {missing_file}. Check the file name or location.")


# Common file modes:
# "r" = read an existing file
# "w" = write; create a file or replace its existing contents
# "a" = append; add content to the end of a file


#JSON HANDLING
import json

# PART 1: THE DATA (Python Dictionary)
# Writing a Python dictionary to a JSON file
data = {
    "name": "Kelvin",
    "age": 24,
    "level": "Intermediate",
    "gpa": 3.5,
    "is_student": True,     #Python True becomes JSON true (lowercase)
    "courses": ["Math", "Python", "Physics"],
    "scores": {
        "Math": 90,
        "Python": 85,
        "Physics": 78,
    },
}
# PART 2: SERIALIZATION (Python Dictionary -> JSON String)
# Convert the dictionary to a JSON string with indentation for readability and write it to a file.
# "w" = write mode; creates the file if it doesn't exist or overwrites it if it does.
json_string = json.dumps(data, indent = 4)  # Convert the dictionary to a JSON string with indentation for readability.
with open("data.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_string)
print(f"Created: data.json")


# PART 3: DESERIALIZATION (JSON String -> Python Dictionary)
# Read the JSON string from the file and convert it back to a Python dictionary.
with open("data.json", "r", encoding="utf-8") as json_file:
    text_from_file = json_file.read()  # Read the JSON string from the file.
    data_from_json = json.loads(text_from_file)  # Convert the JSON string back to a Python dictionary.
print("\n--- Data read from JSON file ---")
print(data_from_json)


# PART 4: USING THE DATA FROM THE JSON FILE
# Accessing values from the deserialized dictionary.
print(f"Name: {data_from_json['name']}")  # Access the name value
print(f"Age: {data_from_json['age']}")    # Access the age value
print(f"GPA: {data_from_json['gpa']}")    # Access the GPA value
print(f"Is Student: {data_from_json['is_student']}")  # Access the boolean value
print(f"Courses: {data_from_json['courses']}")  # Access the list of courses
print(f"Math Score: {data_from_json['scores']['Math']}")  # Access the nested dictionary value for Math score
print(f"Python Score: {data_from_json['scores']['Python']}")  # Access the nested dictionary value for Python score
print(f"Physics Score: {data_from_json['scores']['Physics']}")  # Access the nested dictionary value for Physics score
print(f"All Scores: {data_from_json['scores']}")  # Access the entire nested dictionary of scores
print(f"Keys in data: {list(data_from_json.keys())}")  # List all keys in the dictionary
print(f"Values in data: {list(data_from_json.values())}")  # List all values in the dictionary
print(f"Items in data: {list(data_from_json.items())}")  # List all key-value pairs in the dictionary
print(f"Number of keys in data: {len(data_from_json)}")  # Count the number of keys in the dictionary
print(f"Is 'name' a key in data? {'name' in data_from_json}")  # Check if 'name' is a key in the dictionary
print(f"Is 'address' a key in data? {'address' in data_from_json}")  # Check if 'address' is a key in the dictionary

print(f"Average Score: {sum(data_from_json['scores'].values()) / len(data_from_json['scores'])}")  # Calculate the average score

print((f"Courses: {', '.join(data_from_json['courses'])}"))  # Join the list of courses into a single string

print(f"First Course: {data_from_json['courses'][0]}")  # Access the first course in the list
print(f"Last Course: {data_from_json['courses'][-1]}")  # Access the last course in the list

#Looping Through the nested scores dictionary.
for subject, score in data_from_json['scores'].items():
    print(f"{subject}: {score}")

# PART 5: MODIFYING THE DATA AND WRITING BACK TO JSON (UPDATE CYCLE)
# Update the GPA and add a new course to the list of courses.
data_from_json['gpa'] = 4.3  # Update the GPA value
data_from_json['courses'].append("Data Science")  # Add a new course to the list

#SAVE THE UPDATED DATA BACK TO THE JSON FILE
updated_string = json.dumps(data_from_json, indent=4)  # Convert the updated dictionary back to a JSON string
with open("data.json", "w", encoding="utf-8") as json_file:
    json_file.write(updated_string)  # Write the updated JSON string back to the file
print("\n--- Updated data written back to data.json ---")

# PART 6: READING THE UPDATED JSON FILE TO VERIFY CHANGES
with open("data.json", "r", encoding="utf-8") as json_file:
    updated_text_from_file = json_file.read()  # Read the updated JSON string from the file
    updated_data_from_json = json.loads(updated_text_from_file)  # Convert it back to a Python dictionary
print("\n--- Data read from updated JSON file ---")
print(updated_data_from_json)  # Print the updated dictionary to verify changes
