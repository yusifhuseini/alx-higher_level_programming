#!/usr/bin/python3

"""
A test module for Rectangle area method
"""

import unittest
from models.square import Square


class TestMethodSquareArea(unittest.TestCase):

    def setUp(self):
        self.s = Square(3, 5, 1, 3)

    def tearDown(self):
        del self.s

    def test1WithValidHeightAndWidth(self):
        area = self.s.area()
        self.assertEqual(area, 9)

    def test2WithModifiedAttributes(self):
        self.s.size = 10
        area = self.s.area()
        self.assertEqual(area, 100)

    def test3WithArgument(self):
        with self.assertRaises(TypeError):
            self.s.area(2, 3)
