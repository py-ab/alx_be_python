#!/usr/bin/python3
"""
Module for safe division.
"""

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling potential errors.

    Args:
        numerator: The numerator.
        denominator: The denominator.

    Returns:
        The result of the division, or an error message if division by zero or
        non-numeric input is encountered.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

if __name__ == "__main__":
    # Example usage (for testing the function independently)
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))
    print(safe_divide("ten", 5))

