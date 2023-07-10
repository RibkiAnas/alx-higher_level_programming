#!/usr/bin/python3
"""
Defines Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class called Square that inherits
    from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance
        with the given size.

        Args:
            size: The width of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
