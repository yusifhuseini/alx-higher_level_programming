#!/usr/bin/Python3

"""
A module: Defines a function that converts native objects to json string
"""

json = __import__('json')


def to_json_string(my_obj):
    """
    Converts python native objects to json string

    Args:
        my_obj (str): python string object

    Returns:
        string (json): JSON representation of my_obj
    """
    return json.dumps(my_obj)
