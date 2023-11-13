#!/usr/bin/python3

"""
A test module for Rectangle area method
"""

import unittest
from models.rectangle import Rectangle


class TestMethodRectangleArea(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(3, 5, 1, 3)

    def tearDown(self):
        del self.r

    def test1WithValidHeightAndWidth(self):
        area = self.r.area()
        self.assertEqual(area, 15)

    def test2WithModifiedAttributes(self):
        self.r.height = 10
        self.r.width = 10
        area = self.r.area()
        self.assertEqual(area, 100)

    def test3WithArgument(self):
        with self.assertRaises(TypeError):
            self.r.area(2, 3)
