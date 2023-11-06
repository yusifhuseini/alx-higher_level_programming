#!/usr/bin/python3

"""
A module: Defines a function that determines
if an obj is a direct/indirect instance of a given class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: instance of a class
        a_class: name of a class

    Returns:
        boolean: `True`, if `obj` is a
        direct/indirect instance of `a_class` else `False`
    """
    return isinstance(obj, a_class)
