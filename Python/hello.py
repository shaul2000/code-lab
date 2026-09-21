print("Hello World") # Prints a basic greeting to the screen
print(5 + 5) # Adds two numbers and prints the result: 10

name = "Kelvin" #str = text (must be in quotes)
age = 24 #int = whole number
gpa = 3.5 #float = decimal number
is_student = True #bool = true or false

print("My name is " + name) # Combines text and a variable into one message
print("I am " + str(age) + " years old") # Converts age to text before joining it with the sentence
print("My GPA is " + str(gpa)) # Converts the float to text before printing it
print("I am a student: " + str(is_student)) # Converts the boolean to text so it can be printed

print(type(age)) # Shows the data type of age (it should be <class 'int'>)

x = "10" #this is a string, not an integer
Y = int(x) #this converts the string to an integer
print(type(Y)) # Shows that Y is now an integer after conversion
print(type(x)) # Shows that x is still a string
print( x + x) # Concatenates the string twice, so "10" + "10" becomes "1010"
print( Y + Y) # Adds the integer values, so 10 + 10 = 20
print(Y + 30) # Adds 30 to the integer value of Y, giving 40

name = input("What is your name? ") #this will ask the user for input
age = input("What is your age? ") #this will ask the user for input
print("Hello " + name + ", you are " + age + " years old.") # Prints a greeting using the user's input
# input() always returns a string, so you must convert it to int before doing math
# This is why age is kept as text here instead of being added to a number

input("Press enter to exit") # Pauses the program until the user presses Enter


name = "Kelvin"
height = 1.75 #float = decimal number
gpa = 3.5 #float = decimal number
is_student = True #bool = true or false

print("Name:", name) # Prints the person's name with a label
print("Height:", height) # Prints the height value with a label
print("GPA:", gpa) # Prints the GPA with a label
print("Is student:", is_student) # Prints the boolean value with a label

age_str = "24" #string
age_int = int(age_str) #convert string to integer

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
new_text = text.replace("morning", "afternoon") #replace "morning" with "afternoon"
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

student = { #This is a Dictionary
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

del car["color"] # Removes the color key and its value
print(f"Car Information{car}")

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
print(f"Student Country:{ift_student["address"] ["country"]}")

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