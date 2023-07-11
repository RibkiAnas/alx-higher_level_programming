#!/usr/bin/python3
"""
Define a to_json_string function
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON
    representation of an object (string)
    """
    return json.dumps(my_obj)
