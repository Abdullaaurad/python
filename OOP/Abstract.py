from abc import ABC, abstractmethod    #Important

class Shape(ABC): 
    @abstractmethod                     #Best to use it
    def area(self):                     #Can only be defined inside another derived class of the base class
        pass           

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Area of the circle:", circle.area())  # Output: Area of the circle: 78.5
print("Area of the rectangle:", rectangle.area())  # Output: Area of the rectangle: 24
