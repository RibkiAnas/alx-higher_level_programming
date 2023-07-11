#!/usr/bin/python3
"""
Define a Student class
"""


class Student:
    """
    Defines a student with first name,
    last name, and age attributes
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with
        the given first name, last name,
        and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation
        of the Student object
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {d: getattr(self, d)
                    for d in attrs
                    if hasattr(self, d)}
        return self.__dict__
