#!/usr/bin/python3
"""
Defines base_geometry class
"""


class BaseGeometry:
    """
    A class called BaseGeometry with a public
    instance method that raises an exception.
    """
    def area(self):
        """
        Raises an exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")
