#!/usr/bin/python3
"""Define a function add_integer"""


def add_integer(a, b=98):
    """
    This function adds two integers or floats
    and returns their sum as an integer.

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.
   """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
