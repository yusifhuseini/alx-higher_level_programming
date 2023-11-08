#!/usr/bin/python3

"""
A module: Defines a class `Student`
"""


class Student:
    """
    A Student class

    Methods:
        __init__: instantiation method
        to_json: retrives dictionary representation of class instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation method

        Args:
            first_name (str): instance first name
            last_name (str): instance last name
            age (int): instance age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a `Student` instance
        """
        return self.__dict__
