#!/usr/bin/python3

"""
A module: Defines a lookup function
"""


def lookup(obj):
    """
    Args:
        obj: instance of a class

    Returns:
        (list): a list of available obj attributes and methods
    """
    return dir(obj)
