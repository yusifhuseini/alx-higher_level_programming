#!/usr/bin/python3

"""
A test module for Rectangle display
"""

import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle


class TestRectangleDisplay(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(2, 3)

    def tearDown(self):
        del self.r

    def checkOutput(self, expected):
        with patch('sys.stdout', new=StringIO()) as fakeOut:
            self.r.display()
            self.assertEqual(fakeOut.getvalue(), expected)

    def test1WithoutXandY(self):
        expected = "##\n##\n##\n"
        self.checkOutput(expected)

    def test2WithX(self):
        self.r.x = 1
        expected = " ##\n ##\n ##\n"
        self.checkOutput(expected)

    def test3WithY(self):
        self.r.y = 2
        expected = "\n\n##\n##\n##\n"
        self.checkOutput(expected)

    def test4WithXandY(self):
        self.r.x = 1
        self.r.y = 2
        expected = "\n\n ##\n ##\n ##\n"
        self.checkOutput(expected)


class TestRectangleString(unittest.TestCase):

    def test1WithoutXandY(self):
        r = Rectangle(3, 5)
        expected = "[Rectangle] ({}) 0/0 - 3/5".format(r.id)
        self.assertEqual(str(r), expected)

    def test2WithX(self):
        r = Rectangle(3, 5, 6)
        expected = "[Rectangle] ({}) 6/0 - 3/5".format(r.id)
        self.assertEqual(str(r), expected)

    def test3WithXandY(self):
        r = Rectangle(3, 5, 6, 7)
        expected = "[Rectangle] ({}) 6/7 - 3/5".format(r.id)
        self.assertEqual(str(r), expected)

    def test4WithXandYandId(self):
        r = Rectangle(3, 5, 6, 7, 8)
        expected = "[Rectangle] (8) 6/7 - 3/5"
        self.assertEqual(str(r), expected)


class TestRectangleDictionary(unittest.TestCase):

    def testOutput(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected = {'id': 5, 'x': 3, 'y': 4, 'width': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), expected)

    def testObjectChange(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def testWithArgs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(4)
