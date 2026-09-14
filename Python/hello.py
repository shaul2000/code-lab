print("Hello World")
print(5 + 5)

name = "Kelvin" #str = text (must be in quotes)
age = 24 #int = whole number
gpa = 3.5 #float = decimal number
is_student = True #bool = true or false

print("My name is " + name)
print("I am " + str(age) + " years old")
print("My GPA is " + str(gpa))
print("I am a student: " + str(is_student)) 

print(type(age)) #prints the type of variable

x = "10" #this is a string, not an integer
Y = int(x) #this converts the string to an integer
print(type(Y)) #prints the type of variable
print(type(x)) #prints the type of variable
print( x + x) #this will print 1010 because x is a string
print( Y + Y) #this will print 20 because Y is an integer
print(Y + 30) #this will print 40 because Y is an integer

name = input("What is your name? ") #this will ask the user for input
age = input("What is your age? ") #this will ask the user for input
print("Hello " + name + ", you are " + age + " years old.") 
#input() will always return a string, so if you want to use the input as an 
# integer, you will need to convert it using int(), that's why we don't do math with age here

input("Press enter to exit") #this will wait for the user to press enter before closing the program


name = "Kelvin"
height = 1.75 #float = decimal number
gpa = 3.5 #float = decimal number
is_student = True #bool = true or false

print("Name:", name)
print("Height:", height)
print("GPA:", gpa)
print("Is student:", is_student)

age_str = "24" #string
age_int = int(age_str) #convert string to integer

next_year = age_int + 1 #add 1 to the integer value of age
print("Next year, I will be", next_year, "years old.") #print the value of next_year

print(name.upper()) #convert name to uppercase
print(name.lower()) #convert name to lowercase

sentence = "Python is a great programming language."
words = sentence.split() #split the sentence into a list of words
print(words) #print the list of words
print(words[0]) #print the first word in the list
print(words[-1]) #print the last word in the list


text = "Hello, Good morning, how are you?"
new_text = text.replace("morning", "afternoon") #replace "morning" with "afternoon"
print(new_text) #print the new text
count = text.count("o") #count the number of occurrences of "o" in the text
print("The letter 'o' appears", count, "times in the text.") #print


word = "Information"
print(word[0]) #print the first character of the word
print(word[6]) #print the seventh character of the word
print(word[-1]) #print the last character of the word
print(word[0:3]) #print the first three characters of the word
print(word[3:6]) #print the fourth to sixth characters of the word
print(word[6:]) #print the seventh character to the end of the word
print(word[:6]) #print the first six characters of the word
print(word[::2]) #print every second character of the word
print(word[::-1]) #print the word in reverse order


name = "Kelvin"
age = 24

# Old way (hard to read)
print("My name is " + name + " and I am " + str(age))

# New way (f-string)
print(f"My name is {name} and I am {age}")


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