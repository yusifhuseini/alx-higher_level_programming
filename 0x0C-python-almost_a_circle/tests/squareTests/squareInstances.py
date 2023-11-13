#!/usr/bin/python3


"""
A test module for Rectangle instantiation
"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareInstantiation(unittest.TestCase):

    def testInstantiateWithoutParams(self):
        with self.assertRaises(TypeError):
            Square()

    def testIsBaseInstance(self):
        self.assertIsInstance(Square(2), Base)

    def testIsRectangleInstance(self):
        self.assertIsInstance(Square(2), Rectangle)

    def testInstantiateWithOneParam(self):
        s1 = Square(2)
        s2 = Square(2)
        self.assertEqual(s1.id + 1, s2.id)

    def testInstantiateWithTwoParams(self):
        s1 = Square(1, 2)
        s2 = Square(1, 2)
        self.assertEqual(s1.id + 1, s2.id)

    def testInstantiateWithThreeParams(self):
        s1 = Square(1, 2, 3)
        s2 = Square(1, 2, 3)
        self.assertEqual(s1.id + 1, s2.id)

    def testInstantiationWithFourParams(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, s2.id)

    def testInstantiateWithExcessParams(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def testPrivateAccessRaises(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            s.__size
            s.__width
            s.__height
            s.__x
            s.__y

    def testGetters(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def testSetters(self):
        s = Square(2, 3, 4, 5)
        s.size = 6
        self.assertEqual(s.size, 6)
        s.size = 7
        self.assertEqual(s.width, 7)
        s.size = 10
        self.assertEqual(s.height, 10)
        s.x = 8
        self.assertEqual(s.x, 8)
        s.y = 9
        self.assertEqual(s.y, 9)
