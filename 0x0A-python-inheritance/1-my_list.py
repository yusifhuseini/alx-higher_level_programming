#!/usr/bin/python3

"""
A module: Defines a class 'MyList', that inherits from 'list'

TODO:
    * Defines a public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    Custom class that inherits from builtin 'list' class
    """
    def print_sorted(self):
        """
        A method to print list in an ascending order
        """
        print(sorted(self))
