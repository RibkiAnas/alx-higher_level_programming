#!/usr/bin/python3
"""
Defines MyList class that inherits from
list class
"""

class MyList(list):
    """
    A class that inherits from the built-in
    list class.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in
        ascending order.
        """
        print(sorted(self))
