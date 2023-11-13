#!/usr/bin/python3


"""
A test module for Rectangle instantiation
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):

    def testInstantiateWithoutParams(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testInstantiateWithOneParam(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def testRectangleIsBaseInstance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def testInstantiateWithParamsA(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)

    def testInstantiateWithParamsB(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)

    def testInstantiateWithParamsC(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)

    def testInstantiateWithFiveParams(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def testInstantiateWithExcessParams(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def testPrivateAccessRaises(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            r.__width
            r.__height
            r.__height
            r.__x
            r.__y

    def testGetters(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def testSetters(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        self.assertEqual(r.width, 6)
        r.height = 7
        self.assertEqual(r.height, 7)
        r.x = 8
        self.assertEqual(r.x, 8)
        r.y = 9
        self.assertEqual(r.y, 9)
