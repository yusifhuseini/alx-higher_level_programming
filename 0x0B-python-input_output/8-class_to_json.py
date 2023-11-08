#!/usr/bin/python3

"""
A module: Defines a function that returns the dictionary
description with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Creates a dictionary description of all class attributes

    Args:
        obj (class instance): instance of a class

    Returns:
        (dict): dictionary of attributes
    """
    try:
        return obj.__dict__
    except AttributeError:
        return dict()
