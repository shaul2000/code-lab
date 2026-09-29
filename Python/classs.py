#Create a class of shape and set name, width, height of the shape with the method to print "I am the first shape method"
class Shape:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def describe(self):
        print("I am the first shape method.")


# Create a rectangle shape object from the Shape class above
rectangle = Shape("Rectangle", 10, 5)
print(rectangle.name, rectangle.width, rectangle.height)
rectangle.describe()