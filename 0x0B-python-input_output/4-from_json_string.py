#!/usr/bin/Python3

"""
A module: Defines a function that converts json string to python native data
"""

json = __import__('json')


def from_json_string(my_str):
    """
    Converts json string to python native objects

    Args:
        my_str (json): json string

    Returns:
        obj (python native): python native representation of my_str
    """
    return json.loads(my_str)
