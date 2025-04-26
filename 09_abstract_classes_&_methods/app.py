# 9. Abstract Classes and Methods
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementing the abstract method
    

r1 = Rectangle(5, 10)
r2 = Rectangle(7, 3)
print(f"Area of Rectangle 1: {r1.area()}")  # Output: Area of Rectangle 1: 50
print(f"Area of Rectangle 2: {r2.area()}")  # Output: Area of Rectangle 2: 21