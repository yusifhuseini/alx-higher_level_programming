#!/usr/bin/python3

"""
A module: Defines a Rectangle class, which inherits the `Base` class
"""

from .base import Base


class Rectangle(Base):
    """
    Extends the Base class and defines more instance attributes

    Attributes:
        Instance Attributes:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)

        Class Attributes:
            __nb_objects (int)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate(attr, value):
        """
        Args:
            attr (int): attribute to value validate

        raises:
            TypeError (Exception): if value is not an integer
            ValueError (Exception): if width or height <= 0 or if x or y < 0
        """
        if type(value) != int:
            raise TypeError(f'{attr} must be an integer')
        if (attr == 'width' or attr == 'height') and value <= 0:
            raise ValueError(f'{attr} must be > 0')
        if (attr == 'x' or attr == 'y') and value < 0:
            raise ValueError(f'{attr} must be >= 0')
        return value

    @property
    def width(self):
        """Gets private width"""
        return self.__width

    @property
    def height(self):
        """Gets private height"""
        return self.__height

    @property
    def x(self):
        """Gets private x"""
        return self.__x

    @property
    def y(self):
        """Gets private y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        self.__width = self._validate('width', value)

    @height.setter
    def height(self, value):
        """Sets height attribute"""
        self.__height = self._validate('height', value)

    @x.setter
    def x(self, value):
        """Sets x attribute"""
        self.__x = self._validate('x', value)

    @y.setter
    def y(self, value):
        """Sets y attribute"""
        self.__y = self._validate('y', value)

    def area(self):
        """
        Calculates area of a Rectangle instance

        Returns:
            area (int): product of width and height
        """
        return (self.width * self.height)

    def display(self):
        """
        Creates a 2D display of the Rectangle instance
        """
        print("\n" * self.y, end="")
        for w in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def update(self, *args, **kwargs):
        """
        Assigns first 5 values of args to attributes

        Args:
            args (tuple): a tuple of positional arguments
        """
        attr = ('id', 'width', 'height', 'x', 'y')
        if args and len(args) > 0:
            for i in range(len(args)):
                if i > 0 and i <= 4:
                    setattr(self, attr[i], args[i])
                elif i == 0:
                    super().__init__(args[i])
        else:
            for key, value in kwargs.items():
                if key in attr:
                    if key == 'id':
                        super().__init__(value)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        String representation of class instance
        """
        return """[{}] ({}) {}/{} - {}/{}""".format(self.__class__.__name__,
                                                    self.id, self.x, self.y,
                                                    self.width, self.height)

    def to_dictionary(self):
        """
        Returns:
            dictionary: the dictionary representation of a Retangle instance
        """
        return {'x': self.x, 'y': self.y,
                'id': self.id, 'width': self.width, 'height': self.height}
