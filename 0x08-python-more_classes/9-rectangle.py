#!/usr/bin/python3

"""
A Rectangle class that extends module 7-rectangle.py

TODO:
    * Class method def square(cls, size=0): that returns a new
    Rectangle instance with 'width == height == size'
"""


class Rectangle:
    """
    Attributes:
        Instace attributes:
            width (int)
            height (int)

        Class attributes:
            number_of_instances (int)
            print_symbol (any)
    """
    number_of_instances = 0
    print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares class objects

        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)

        Returns:
            The biggest of both or rect_1 if they are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1 > rect_2 or rect_1 == rect_2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new instance of class

        Args:
            size (int)

        Returns:
            object (Rectangle)
        """
        return Rectangle(size, size)

    def __str__(self):
        """
        String representation of Class instances

        Returns:
            string (str)
        """
        string = ""
        if self.width > 0 and self.height > 0:
            for i in range(self.height - 1):
                string += str(self.print_symbol) * self.width + "\n"
            string += str(self.print_symbol) * self.width
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
