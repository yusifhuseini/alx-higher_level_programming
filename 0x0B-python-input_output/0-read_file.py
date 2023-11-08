#!/usr/bin/Python3

"""
A module: Defines a function that reads from a file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints to stdout

    Args:
        filename (str): name of filename
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
