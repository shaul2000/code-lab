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
    
    


class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    
    def drive(self):
        print(f"I am driving a {self.name}, It is a {self.color} color")
    
    def __str__(self):
        return f"{self.name}"
        
car1 = Car("GLE", 363, "Black")
print(car1.name, car1.model, car1.color)
car1.drive()

car2 = Car("Corolla", 2021, "White")
print(car2.name, car2.model, car2.color)
car2.drive()

print(f"My first object is: {car1}")
print(f"My second object is: {car2}")

#Inheritance:
class Computer(Car):
    pass
laptop = Computer("Dell", "Core i5", "Black")
print(laptop.color, laptop.name, laptop.model)
