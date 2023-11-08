#!/usr/bin/Python3

"""
A module: Defines a function that writes python
native object to a text file in json representaion
"""

json = __import__('json')


def save_to_json_file(my_obj, filename):
    """
    Writes python native object to a text file in json representation

    Args:
        my_obj (json): python native object
        filename (str): name of json file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
