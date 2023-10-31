#!/usr/bin/python3

"""
A name-printing module.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a name.

    Args:
        first_name (str): the first name to print.
        last_name (str): the last name to print.

    Raises:
        TypeError: if either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
