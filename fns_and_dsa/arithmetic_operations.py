#!/usr/bin/python3

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the given inputs.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', or 'divide').

    Returns:
        float: The result of the operation, or an error message if the operation is invalid or division by zero occurs.
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero."  # Or return None, or raise an exception
        else:
            return num1 / num2
    else:
        return "Invalid operation."  # Or return None, or raise an exception
