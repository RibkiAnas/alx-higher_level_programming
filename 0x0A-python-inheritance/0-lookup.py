#!/usr/bin/python3
"""0-lookup.py"""


def lookup(obj):
    """
    Returns a list of available attributes
    and methods of an object.
    """
    return [attr for attr in dir(obj)]
