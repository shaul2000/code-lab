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

print("My name is " + name)