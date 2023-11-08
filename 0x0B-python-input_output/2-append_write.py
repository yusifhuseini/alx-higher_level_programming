#!/usr/bin/Python3

"""
A module: Defines a function that appends text to a file
"""


def append_write(filename="", text=""):
    """
    Appends text to a file in UTF8 format

    Args:
        filename (str): name of filename
        text (str): text to be appended to file

    Returns:
        int: number of characters appended
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
