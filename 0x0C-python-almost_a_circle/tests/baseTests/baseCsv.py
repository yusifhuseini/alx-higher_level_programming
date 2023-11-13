#!/usr/bin/python3

"""
A test module for Base class csv file interaction
"""

import os
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSaveToCsvFile(unittest.TestCase):

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def testCsvFileCreation(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        self.assertTrue(os.path.exists("Rectangle.csv"))

        s = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s])
        self.assertTrue(os.path.exists("Square.csv"))

    def testCsvFileContentAndLength(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertTrue("1,2,3,4,5", file.read())

        s = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s])
        with open("Square.csv", encoding='utf-8') as file:
            self.assertTrue("1,2,3,4", file.read())

    def testCsvFileOverWrite(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        r = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertTrue("6,7,8,9,10", file.read())

    def testWithNone(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertEqual("\n", file.read())

    def tesWithAnEmptyList(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertEqual("\n", file.read())

    def testWithNoArguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def testWithExcessArguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], [])


class TestLoadFromCsvFile(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def testCheckLinesAndLineValues(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file_csv([r1, r2])
        rects = Rectangle.load_from_file_csv()
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))
        self.assertTrue(all(type(r) == Rectangle for r in rects))

        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file_csv([s1, s2])
        squares = Square.load_from_file_csv()
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))
        self.assertTrue(all(type(s) == Square for s in squares))

    def testCsvFileDoesNoExist(self):
        response = Square.load_from_file_csv()
        self.assertEqual([], response)

    def testWithExcessArguments(self):
        with self.assertRaises(TypeError):
            Square.load_from_file_csv([], [])
