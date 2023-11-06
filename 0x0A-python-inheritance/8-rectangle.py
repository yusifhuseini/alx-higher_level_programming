#!/usr/bin/python3

"""
A module: Create a sub class from `BaseGeometry`
class defined in module `7-base_geometry`
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
