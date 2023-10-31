#!/usr/bin/python3
"""
A module that showcases locked class
instance attribute
"""


class LockedClass:
    """
    Prevent dynamic creation of attributes by new instances
    """
    __slots__ = ('first_name',)

    def __init__(self):
        pass
