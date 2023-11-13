#!/usr/bin/python3

"""
A test module to validate rectangle width attribute
"""

import unittest

from models.square import Square


class TestSquareSize(unittest.TestCase):

    def testInvalidSizeType(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            """ size as None """
            Square(None)

            """ size as float """
            Square(3.3)

            """ size as infinite float """
            Sqaure(float('inf'))

            """ size as 'nan' """
            Sqaure(float('nan'))

            """ size as string """
            Sqaure("Hey")

            """ size as List """
            Square([3, 4])

            """ size as tuple """
            Square((1,))

            """ size as dictionary """
            Square({'a': 1})

            """ size as set """
            Square({1, 2})

            """ size as set """
            Square(True)

            """ size as bytes """
            Square(b'Alx')

    def testWithZeroSizeValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def testWithNegativeSizeValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)


class TestSquareX(unittest.TestCase):

    def testInvalidXType(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            """ x as None """
            Square(5, None)

            """ x as float """
            Square(5, 4.4)

            """ x as infinite float """
            Square(5, float('inf'))

            """ x as 'nan' """
            Square(5, float('nan'))

            """ x as string """
            Square(5, "Hey")

            """ x as List """
            Square(5, [3, 4])

            """ x as tuple """
            Square(5, (1,))

            """ x as dictionary """
            Square(5, {'a': 1})

            """ x as set """
            Square(5, {1, 2})

            """ x as set """
            Square(5, True)

            """ x as bytes """
            Square(5, b'Alx')

    def testInvalidXValue(self):

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            """ x = -ve """
            Square(5, -1)


class TestSquareY(unittest.TestCase):

    def testInvalidYType(self):

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            """ y as None """
            Square(5, 4, None)

            """ y as float """
            Square(5, 4, 4.4)

            """ y as infinite float """
            Square(5, 4, float('inf'))

            """ y as 'nan' """
            Square(5, 4, float('nan'))

            """ y as string """
            Square(5, 4, "Hey")

            """ y as List """
            Square(5, 4, [3, 4])

            """ y as tuple """
            Square(5, 4, (1,))

            """ y as dictionary """
            Square(5, 4, {'a': 1})

            """ y as set """
            Square(5, 4, {1, 2})

            """ y as set """
            Square(5, 4, True)

            """ y as bytes """
            Square(5, 4, b'Alx')

    def testInvalidYValue(self):

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            """ y = -ve """
            Square(5, 4, -1)
