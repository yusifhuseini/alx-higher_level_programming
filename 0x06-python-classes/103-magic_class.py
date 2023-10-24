#!/usr/bin/python3
"""
Deciphering Python bytecodes

Todos:
    My magician game is on, ah gat this.
"""
import math


class MagicClass:
    """
    A Magic circle class

    Attributes:
        __init__ (function): class instance trigger
        area (function): area of a circle
        circumference (function): object circumference
    """

    def __init__(self, radius=0):
        """
        Instantiation

        Args:
            self (MagicClass): instance of class
            radius (int): instance attribute
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle

        Returns:
            area (int): product of radius and radius
        """
        return (self.radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of the square

        Returns:
            circumference (int): length of the circle
        """
        return (2 * math.pi * self.radius)
