#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle(BaseGeometry):
    """
    A class called Rectangle that inherits
    from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance
        with the given width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the
            rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
