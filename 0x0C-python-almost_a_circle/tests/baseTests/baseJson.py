#!/usr/bin/python3

"""
A test module for Base json conversion
"""

import os
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestJsonStringFormat(unittest.TestCase):

    def testRectangleType(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertIsInstance(Base.to_json_string([r.to_dictionary()]), str)

    def testRectangleJsonLength(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(52, len(Base.to_json_string([r.to_dictionary()])))

    def testSquareType(self):
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(Base.to_json_string([s.to_dictionary()]), str)

    def testSquareJsonLength(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(38, len(Base.to_json_string([s.to_dictionary()])))

    def testWithNone(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def testWithEmptyList(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def testWithoutArguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def testWithMoreArgments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestSaveToJsonFile(unittest.TestCase):

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def testJsonFileCreation(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def testValidateJsonContentLength(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", encoding='utf-8') as file:
            self.assertEqual(52, len(file.read()))

        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual(38, len(file.read()))

    def testJsonFileOverwrite(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", encoding='utf-8') as file:
            self.assertEqual(52, len(file.read()))
        r = Rectangle(11, 22, 33, 44, 55)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", encoding='utf-8') as file:
            self.assertEqual(57, len(file.read()))

        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual(38, len(file.read()))
        s = Square(11, 22, 33, 44)
        Square.save_to_file([s])
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual(42, len(file.read()))

    def testSaveNoneValueToJson(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", encoding="utf-8") as file:
            self.assertEqual("[]", file.read())

        Square.save_to_file(None)
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual("[]", file.read())

    def testSaveEmptyListToJson(self):
        Square.save_to_file([])
        with open("Square.json", encoding="utf-8") as file:
            self.assertEqual("[]", file.read())

    def testSaveToJsonWithoutArguments(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def testSaveToJsonWithExcessArguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestFromJsonStringToPythonList(unittest.TestCase):

    def testTypeCheck(self):
        pyList = [{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]
        jsonString = Rectangle.to_json_string(pyList)
        J2P = Rectangle.from_json_string(jsonString)
        self.assertEqual(type(J2P), list)

    def testFromJsonToList(self):
        pyList = [{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]
        jsonString = Rectangle.to_json_string(pyList)
        J2P = Rectangle.from_json_string(jsonString)
        self.assertEqual(J2P, pyList)

        pyList = [{"id": 1, "x": 2, "y": 3, "size": 4}]
        jsonString = Square.to_json_string(pyList)
        J2P = Square.from_json_string(jsonString)
        self.assertEqual(J2P, pyList)

    def testWithNoneArgument(self):
        self.assertEqual(Base.from_json_string(None), [])

    def testWithEmptyJsonStringArray(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def testWithNoArgument(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testWithExcessArguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])


class TestLoadFromJsonFile(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def testCheckLinesAndLineValues(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 6, 7, 8, 9)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))
        self.assertTrue(all(type(r) == Rectangle for r in rects))

        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))
        self.assertTrue(all(type(s) == Square for s in squares))

    def testJsonFileDoesNotExist(self):
        response = Square.load_from_file()
        self.assertEqual(response, [])

    def testWithExessArguments(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])
