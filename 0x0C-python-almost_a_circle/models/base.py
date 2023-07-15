#!/usr/bin/python3
"""
Define class Base.
"""


class Base:
    """
    Base class to manage id attribute in all
    future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
