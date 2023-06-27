#!/usr/bin/python3
"""define a class Square"""


class Square:
    """This is an empty class that defines a square."""
    def __init__(self, size=0):
        """This method initializes the size attribute
        of the Square instance."""
        self.size = size

    @property
    def size(self):
        """This method retrieves the size
        attribute of the Square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size attribute
        of the Square instance"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
