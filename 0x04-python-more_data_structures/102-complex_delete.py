#!/usr/bin/python3

"""
    /**
      * Complex delete - deletes keys with a specific value in a dictionary
      * @a_dictionary: dictionary
      * @value: value whose key is to be deleted
      *
      * Return: None
      */
"""


def complex_delete(a_dictionary, value):
    dictB = dict(a_dictionary)
    for idx, item in dictB.items():
        if item == value:
            del a_dictionary[idx]
    return a_dictionary
