#!/usr/bin/python3

"""
A module: Creates a class `Square`
that inherits from `Rectangle` in module `9-rectangle`
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle and overides the instantiation method
    """
    def __init__(self, size):
        """
        Class object instantiation method

        Args:
            self (Square): class instance
            size (int): size of the new Square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        String representation of Sqaure class objects, keeps the parent class
        name
        """
        self.__class__.__name__ = "Rectangle"
        return super().__str__()
