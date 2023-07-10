#!/usr/bin/python3
"""
Defines base_geometry class
"""


class BaseGeometry:
    """
    A class called BaseGeometry with two
    public instance methods.
    """

    def area(self):
        """
        Raises an exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive
        integer.

        Agrs:
            name: The name of the value being
            validated.
            value: The value to validate.
        Raises:
            TypeError: If value is not an
            integer.
            ValueError: If value is less
            than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
