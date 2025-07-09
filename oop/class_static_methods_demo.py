#!/usr/bin/python3
"""
Demonstrates class methods and static methods in Python.
"""

class Calculator:
    """
    A simple calculator class with a static method for addition
    and a class method for multiplication.
    """

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Returns the sum of two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers.
        Prints the calculation type before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

if __name__ == "__main__":
    # Example usage (for testing the class independently)
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
