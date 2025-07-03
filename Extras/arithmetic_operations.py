# arithmetic_operations.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the result of dividing two numbers.
    If the divisor is 0, returns an error message.
    """
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
