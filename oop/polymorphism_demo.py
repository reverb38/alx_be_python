# polymorphism_demo.py

import math

class Shape:
    """Base class for different shapes."""
    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides area() to calculate rectangle area."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides area() to calculate circle area."""
        return math.pi * (self.radius ** 2)

