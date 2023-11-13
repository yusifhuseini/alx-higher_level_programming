#!/usr/bin/python3


"""
A test module to check Base class create method
"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseCreateMethod(unittest.TestCase):

    def testCreateNewRectangleObject(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        rD1 = r1.to_dictionary()
        r2 = Rectangle.create(**rD1)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def testCreateNewSquareObject(self):
        s1 = Square(1, 2, 3, 4)
        sD1 = s1.to_dictionary()
        s2 = Square.create(**sD1)
        self.assertEqual("[Square] (4) 2/3 - 1", str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)
