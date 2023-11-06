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

    def integer_validator(self, name, value):
        """
        Args:
            name (str): string
            value (int): integer

        Raises:
            TypeError (Exception): if value is not type integer
            ValueError (Exception): if value is less than or equal to zero
        """
        if not type(name) == str:
            raise Exception('\'name\' must be a string')
        if not type(value) == int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
