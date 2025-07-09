#!/usr/bin/python3
"""
Demonstrates polymorphism through method overriding with Shape classes.
"""

import math

class Shape:
    """
    Base class for shapes.
    """

    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area method")


class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    """

    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    # Example usage (for testing the classes independently)
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    print(f"The area of the rectangle is: {rectangle.area()}")
    print(f"The area of the circle is: {circle.area()}")
