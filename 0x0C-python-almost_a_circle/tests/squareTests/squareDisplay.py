#!/usr/bin/python3

"""
A test module for Rectangle display
"""

import unittest
from io import StringIO
from unittest.mock import patch

from models.square import Square


class TestSquareDisplay(unittest.TestCase):

    def setUp(self):
        self.s = Square(3)

    def tearDown(self):
        del self.s

    def checkOutput(self, expected):
        with patch('sys.stdout', new=StringIO()) as fakeOut:
            self.s.display()
            self.assertEqual(fakeOut.getvalue(), expected)

    def test1WithoutXandY(self):
        expected = "###\n###\n###\n"
        self.checkOutput(expected)

    def test2WithX(self):
        self.s.x = 1
        expected = " ###\n ###\n ###\n"
        self.checkOutput(expected)

    def test3WithY(self):
        self.s.y = 2
        expected = "\n\n###\n###\n###\n"
        self.checkOutput(expected)

    def test4WithXandY(self):
        self.s.x = 1
        self.s.y = 2
        expected = "\n\n ###\n ###\n ###\n"
        self.checkOutput(expected)


class TestSquareString(unittest.TestCase):

    def test1WithoutXandY(self):
        s = Square(3)
        expected = "[Square] ({}) 0/0 - 3".format(s.id)
        self.assertEqual(str(s), expected)

    def test2WithX(self):
        s = Square(3, 5)
        expected = "[Square] ({}) 5/0 - 3".format(s.id)
        self.assertEqual(str(s), expected)

    def test3WithXandY(self):
        s = Square(3, 5, 6)
        expected = "[Square] ({}) 5/6 - 3".format(s.id)
        self.assertEqual(str(s), expected)

    def test4WithXandYandId(self):
        s = Square(3, 5, 6, 7)
        expected = "[Square] (7) 5/6 - 3"
        self.assertEqual(str(s), expected)


class TestSquareDictionary(unittest.TestCase):

    def testOutput(self):
        s = Square(5, 2, 3, 4)
        expected = {'id': 4, 'x': 2, 'y': 3, 'size': 5}
        self.assertDictEqual(s.to_dictionary(), expected)

    def testObjectChange(self):
        s1 = Square(5, 2, 3, 4)
        s2 = Square(3, 2, 5)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def testWithArguments(self):
        s = Square(5, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)
