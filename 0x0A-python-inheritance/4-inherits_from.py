#!/usr/bin/python3

"""
A module: Defines a function that determines if an obj is an instance
of a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: instance of a class
        a_class: name of a class

    Returns:
        boolean: `True`, if `obj` is a
        direct or indirect instance of `a_class` else `False`
    """
    return (type(obj) != a_class and isinstance(obj, a_class))
