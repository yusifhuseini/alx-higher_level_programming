#!/usr/bin/python3

"""
A Rectangle class that extends module 5-rectangle.py

TODO:
    * Add a public class attribute number_of_instances:
        * Initialized to 0
        * Incremented during each new instance instantiation
        * Decremented during each instance deletion
"""


class Rectangle:
    """
    Attributes:
        Instace attributes:
            width (int)
            height (int)

        Class attributes:
            number_of_instances (int)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Args:
            width (integer)
            height (integer)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Returns:
            width (integer)
        """
        return self.__width

    @property
    def height(self):
        """
        Returns:
            height (integer)
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Args:
            value (integer)
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Args:
            value (integer)
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculate the area of a rectangle

        Returns:
            area (integer):
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle

        Returns:
            perimeter (integer)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """
        String representation of Class instances

        Returns:
            string (str)
        """
        string = ""
        if self.width > 0 and self.height > 0:
            for i in range(self.height - 1):
                string += "#" * self.width + "\n"
            string += "#" * self.width
        return string

    def __repr__(self):
        """
        Canonical string representation of the object

        Returns:
            string (str)
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Defines delete operation when called
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
