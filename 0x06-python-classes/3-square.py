#!/usr/bin/python3
"""define a class Square"""


class Square:
    """This is an empty class that defines a square."""
    def __init__(self, size=0):
        """This method initializes the size attribute
        of the Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returns the current square area."""
        return self.__size ** 2
