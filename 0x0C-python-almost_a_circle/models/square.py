#!/usr/bin/python3

"""
A module: Defines a Square class, which inherits the `Rectangle` class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Extends inherits Rectangle class

    Attributes:
        Instance Attributes:
            size (int): sets width and height attributes
            x (int)
            y (int)
            id (int): instance id

        Class Attributes:
            __nb_objects (int)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation method, calls the parent instantiation method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representaion of class instance
        """
        return """[{}] ({}) {}/{} - {}""".format(self.__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Gets instance size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets instance size

        Args:
            value (int): new value for size
        """
        self.width = self._validate('width', value)
        self.height = self.width

    def update(self, *args, **kwargs):
        """
        Updates class attributes

        Args:
            args (tuple): list of positional arguments
            kwargs (dictionary): dictionary of attributes and new values
        """
        attr = ('id', 'size', 'x', 'y')
        if args and len(args) > 0:
            for i in range(len(args)):
                if i > 0 and i <= 3:
                    setattr(self, attr[i], args[i])
                elif i == 0:
                    self.__init__(self.size, self.x, self.y, args[i])
        else:
            for key, value in kwargs.items():
                if key in attr:
                    if key == 'id':
                        self.__init__(self.size, self.x, self.y, value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns:
            dictionary: a dictionary of instance attributes
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
