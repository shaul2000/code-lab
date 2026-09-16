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


print(5 == 5) # equal to
print(5 != 5) # not equal to
print(5 != 3) # not equal to
print(5 > 3) # greater than
print(5 < 3) # less than
print(3 > 5) # greater than (false)
print(3 < 5) # less than
print(5 >= 5) # greater than or equal to
print(5 <= 5) # less than or equal to
print(3 <= 5) # less than or equal to
print(3 >= 5) # greater than or equal to (false)
print(5 <= 3) # less than or equal to (false)

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or lower")
    


age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter!") #Both must be true
    
if age < 18 or has_ticket:
    print("Special entry allowed.") #Only one needs to be true
    
if not has_ticket:
    print("You do not have a ticket.") #Reverses True to False or False to True
    

    
if 0:
    print("This won't run") #doesn't run because 0 is false
    
if 5:
    print("This WILL run")      # ✅ Runs (5 = True)

if -1:
    print("This WILL also run") # ✅ Runs (-1 = True, it's not zero!)

if "hello":
    print("This runs too")      # ✅ Runs (non-empty text = True)

if "":
    print("Won't run")          # ❌ Skipped (empty text = False)
    
#List Examples
subjects = ["Math", "Python", "Physics"]
print(subjects) #['Math', 'Python', 'Physics']
print(subjects[0]) #"Math" (first item on the list)
print(subjects[-1]) #"Physics" (last object on the list)
print(len(subjects)) # 3 (how many items are on the list)

#Slicing, sorting and searching
nums = [10, 20, 30, 40, 50]
print(nums[1:4]) #[20, 30, 40] ← start included, end excluded
print(nums[::-1]) #[50, 40, 30, 20, 10] ← reversed

#Sorting:
scores = [85, 42, 90, 67]
scores.sort() #sorts the original list in place → [42, 67, 85, 90]
print(sorted(scores, reverse=True)) #Prints the reversed copy of the sorted scores [90, 85, 67, 42] (doesn't change original)
print(scores) #prints the sorted original scores in ascending, nothing changed.

#Searching: (in)
if "Python" in subjects:
    print("Python is on my timetable")
    
courses = ["Math", "Python", "Physics"]    
courses.append("Chemistry") #Adds Chemistry to the list
courses.pop(2) #Removes "Math" from the list 

print(courses)