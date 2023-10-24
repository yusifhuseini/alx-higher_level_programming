#!/usr/bin/python3

"""
A script that creates a class and validates its given attribute
Attributes:
    Square (class): with a valid attribute 'size'
Todo:
    * Private instance attribute: size
    * property setter def 'size(self, value)' to set it
    * size must be an integer, otherwise raise a 'TypeError' exception with
    the message size must be an integer
    * if size is less than 0, raise a 'ValueError' exception with the message
    size must be >= 0
    * Public instance method: 'def area(self)' that returns the current
    square area
    * Square instance can answer to comparators: ==, !=, >, >=, < and <=
    based on the square area
"""


class Square:
    """
        Atrributes:
            __init__ (function): assign and validate attributes
            area (function): calculate area of square
    """
    def __init__(self, size=0):
        """
        Args:
            self (Square): object
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Args:
            self (Square): instance of class
        Return:
            area (int)
        """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """
        Args:
            self (Square): Square instance object
            other (Square): Square instance object

        Returns:
            bool: Equality definition
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Args:
            self (Square): Square instance object
            other (Square): Square instance object
        Returns:
            bool: None equality definition
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Args:
            self (Square): Square instance object
            other (Square): Square instance object
        Returns:
            bool: Greater than definition
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Args:
            self (Square): Square instance object
            other (Square): Square instance object
        Returns:
            bool: Greater than or equals to definition
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Args:
            self (Square): Square instance object
            other (Square): Square instance object
        Returns:
            bool: Less than definition
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Args:
            self (Square): Square instance object
            other (Square): Square instance object
        Returns:
            bool: Less than or equals to definition
        """
        return self.area() <= other.area()
