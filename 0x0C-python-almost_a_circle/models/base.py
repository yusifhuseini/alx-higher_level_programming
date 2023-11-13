#!/usr/bin/python3

"""
A module: Defines a Base class
"""

import os
import csv
import json
import turtle


class Base:
    """
    Project Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation method

        Args:
            id (int): if `id` is not None set instance `id` to `id` value,
            else increase `__nb_object` and assign to `id`
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts Python data objects to JSON strng

        Args:
            list_dictionaries (dictionary): python list of dictionaries

        Returns:
            string (str): "[]" if list_dictionary is empty else JSON format
        """
        if list_dictionaries is None or\
                len(list_dictionaries) == 0 or\
                type(list_dictionaries) != list:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a native Python list

        Args:
            json_string (JSON): string representation of list to be converted
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON representationof list_objs to file

        Args:
            list_objs (list): lists of class instances
        """
        list_objs = [] if list_objs is None else list_objs
        filename = '{}.json'.format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(
                cls.to_json_string([o.to_dictionary() for o in list_objs])
            )

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a class instance, assigns its attributes values in dictionary

        Args:
            dictionary (dict): dictionary containing attribute and values
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(3, 5)
        elif cls.__name__ == 'Square':
            obj = cls(5)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Creates a list of instances from a JSON file with the class name

        Returns:
            list: empty if file does not exist else, list of class instances
        """
        filename = "%s.json" % cls.__name__
        objs = []
        if os.path.exists(filename):
            with open(filename, encoding='utf-8') as file:
                objs = cls.from_json_string(file.read())
            return [cls.create(**obj) for obj in objs]
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of Base subclass instances in a csv file

        Args:
            list_objs (list): list of dictionary representation of instances
        """
        filename = "%s.csv" % cls.__name__
        header = []
        if list_objs is not None and len(list_objs) > 0:
            if all(map(lambda x: isinstance(x, cls), list_objs)):
                header = ['id', 'width', 'height', 'x', 'y']
                if len((list_objs[0]).to_dictionary()) == 4:
                    header = ['id', 'size', 'x', 'y']
        else:
            list_objs = []

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(map(lambda x: x.to_dictionary(), list_objs))

    @classmethod
    def load_from_file_csv(cls):
        """
        Creates a list of instances from a JSON file with the class name

        Returns:
            list: empty if file does not exist else, list of class instances
        """
        filename = "%s.csv" % cls.__name__
        objs = []
        if os.path.exists(filename):
            with open(filename, encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    obj = {}
                    for k, v in line.items():
                        obj[k] = int(v)
                    objs.append(cls.create(**obj))
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws Rectangle and square instances on a GUI
        """
        if list_rectangles is not None and list_rectangles != []:
            for rec in list_rectangles:
                rd = rec.to_dictionary()
                turtle.pu()
                turtle.speed(1)
                turtle.setpos(rd['x'], rd['y'])
                turtle.pd()
                turtle.shape("Rectangle")
                turtle.pensize(3)
                turtle.color("blue", "red")
                turtle.begin_fill()
                turtle.forward(rd['width'])
                turtle.right(90)
                turtle.forward(rd['height'])
                turtle.right(90)
                turtle.forward(rd['width'])
                turtle.right(90)
                turtle.forward(rd['height'])
                turtle.end_fill()
                turtle.pu()

        if list_squares is not None and list_squares != []:
            for sq in list_squares:
                sd = sq.to_dictionary()
                turtle.pu()
                turtle.speed(1)
                turtle.setpos(sd['x'], sd['y'])
                turtle.pensize(3)
                turtle.pd()
                turtle.shape("Square")
                turtle.forward(sd['size'])
                turtle.color("blue", "red")
                turtle.begin_fill()
                turtle.forward(sd['size'])
                turtle.right(90)
                turtle.right(90)
                turtle.forward(sd['size'])
                turtle.right(90)
                turtle.forward(sd['size'])
                turtle.end_fill()
                turtle.pu()
        turtle.exitonclick()
