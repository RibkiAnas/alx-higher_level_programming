#!/usr/bin/python3
"""1-my_list.py"""

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
        sorted_list = sorted(self)
        print(sorted_list)
