#!/usr/bin/Python3

"""
A module: Defines a function that crreates a python
native object from a JSON file
"""

json = __import__('json')


def load_from_json_file(filename):
    """
    Creates a python native object from a JSON file

    Args:
        filename (str): name of json file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.loads(file.read())
