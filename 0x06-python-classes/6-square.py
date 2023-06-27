#!/usr/bin/python3
"""define a class Square"""


class Square:
    """This class defines a square with
    private instance attributes size and
    position."""
    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the size attribute
        of the Square instance."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This method retrieves the position
        attribute of the Square instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the position
        attribute of the Square instance"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or value[0] < 0 or value[1] < 0
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
