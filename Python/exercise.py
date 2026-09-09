My_name = "PAUL AWAJIMIJAN"
My_school_name = "Federal University of Technology, Minna"

def my_second_function():
    print(My_name)
    print(My_school_name)
    
#function invocation
my_second_function()


#Function that will accept 2 numbers and find their product
def find_product(num1, num2):
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
    
    
find_product(12, 14)
find_product(18, 53)
    
 #Finding the quotient of 2 numbers
def findQ(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        quotient = num1 / num2
        print(f"The quotient of {num1} and {num2} is {quotient}")
findQ(27, 3)
findQ(27, 0)