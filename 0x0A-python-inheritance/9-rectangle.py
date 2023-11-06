#!/usr/bin/python3

"""
A module: Improves the `Rectangle` class defined in module `8-rectangle`
that inherits from `BaseGeometry` class defined in module `7-base_geometry`

TODO:
    * Overides the base class `area` method
    * Adds `__str__` method for class instance definition
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class: inherits from class `BaseGeometry` and adds a new class method
    """
    def __init__(self, width, height):
        """
        Instance instantiation method

        Args:
            self (Rectangle): instance of Rectangle
            width (int): positive integer
            height (int): positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of a Rectangle instance

        Returns:
            area (int): product of `__width` and `__height`
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        String representation of class instance

        Returns:
            string (str)
        """
        string = '[{:s}] {:d}/{:d}'.format(self.__class__.__name__,
                                           self.__width, self.__height)
        return string
