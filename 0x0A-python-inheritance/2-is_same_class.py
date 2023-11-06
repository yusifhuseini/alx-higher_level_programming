#!/usr/bin/python3

"""
A module: Defines a function that determines
if an obj is an exact instance of a given class
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: instance of a class
        a_class: name of a class

    Returns:
        boolean: `True`, if `obj` is an instance of `a_class` else `False`
    """
    return (type(obj) == a_class)
