#!/usr/bin/python3

"""
A module: Defines a function `add_attribute`
"""


def add_attribute(obj, attr, value):
    """
    A function that adds a new attribute to an object if it’s possible

    Args:
        obj (instance of a class): instance of a class
        attr (str): attribute to be added to obj
        value (str): value of attribute `attr`

    Raises:
        TypeError (Exception): if an attribute can not be added to `obj`
    """
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr, value)
    else:
        raise TypeError('can\'t add new attribute')
