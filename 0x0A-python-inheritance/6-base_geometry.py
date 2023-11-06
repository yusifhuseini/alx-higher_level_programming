#!/usr/bin/python3

"""
A module: Creates and defines base class:- `BaseGeometry`
"""


class BaseGeometry:
    """
    An Base Geometry class
    """
    def area(self):
        """
        A class method that raises an exception

        Raises:
            Exception: `area() is not implemented`
        """
        raise Exception('area() is not implemented')
