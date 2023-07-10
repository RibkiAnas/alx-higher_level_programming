#!/usr/bin/python3
"""
Defines MyInt class
"""


class MyInt(int):
    """
    A class called MyInt that inherits
    from built-in int class.
    This class inverts the behavior of the
    == and =! operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to invert
        its behavior.
        Returns True if self and other are not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert
        its behavior.
        Returns True if self and other are
        equal, False otherwise.
        """
        return super().__eq__(other)
