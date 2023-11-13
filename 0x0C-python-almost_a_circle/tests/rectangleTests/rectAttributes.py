#!/usr/bin/python3

"""
A test module to validate rectangle width attribute
"""

import unittest

from models.rectangle import Rectangle


class TestRectangleWidth(unittest.TestCase):

    def testInvalidWidthType(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            """ Width as None """
            Rectangle(None, 5)

            """ Width as float """
            Rectangle(3.3, 5)

            """ Width as infinite float """
            Rectangle(float('inf'), 5)

            """ Width as 'nan' """
            Rectangle(float('nan'), 5)

            """ Width as string """
            Rectangle("Hey", 5)

            """ Width as List """
            Rectangle([3, 4], 5)

            """ Width as tuple """
            Rectangle((1,), 5)

            """ Width as dictionary """
            Rectangle({'a': 1}, 5)

            """ Width as set """
            Rectangle({1, 2}, 5)

            """ Width as set """
            Rectangle(True, 2)

            """ Width as bytes """
            Rectangle(b'Alx', 2)

    def testWithZeroWidthValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

    def testWithNegativeWidthValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 5)

    def testWithZeroHeightValue(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def testWithNegativeHeightValue(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -1)


class TestRectangleHeight(unittest.TestCase):

    def testInvalidHeightType(self):

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            """ Height as None """
            Rectangle(5, None)

            """ Height as float """
            Rectangle(5, 3.3)

            """ Height as infinite float """
            Rectangle(5, float('inf'))

            """ Height as 'nan' """
            Rectangle(5, float('nan'))

            """ Height as string """
            Rectangle("Hey", 5)

            """ Height as List """
            Rectangle(5, [3, 4])

            """ Height as tuple """
            Rectangle(5, (1,))

            """ Height as dictionary """
            Rectangle(5, {'a': 1})

            """ Height as set """
            Rectangle(5, {1, 2})

            """ Height as boolean """
            Rectangle(5, True)

            """ Height as bytes """
            Rectangle(5, b'Alx')

    def testInvalidWidthType(self):

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            """ Height = zero """
            Rectangle(5, 0)

            """ Height = -ve """
            Rectangle(5, -1)


class TestRectangleX(unittest.TestCase):

    def testInvalidXType(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            """ x as None """
            Rectangle(3, 5, None)

            """ x as float """
            Rectangle(3, 5, 4.4)

            """ x as infinite float """
            Rectangle(3, 5, float('inf'))

            """ x as 'nan' """
            Rectangle(3, 5, float('nan'))

            """ x as string """
            Rectangle(3, 5, "Hey")

            """ x as List """
            Rectangle(3, 5, [3, 4])

            """ x as tuple """
            Rectangle(3, 5, (1,))

            """ x as dictionary """
            Rectangle(3, 5, {'a': 1})

            """ x as set """
            Rectangle(3, 5, {1, 2})

            """ x as set """
            Rectangle(3, 5, True)

            """ x as bytes """
            Rectangle(3, 5, b'Alx')

    def testInvalidXValue(self):

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):

            """ x = -ve """
            Rectangle(3, 5, -1)


class TestRectangleY(unittest.TestCase):

    def testInvalidYType(self):

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            """ y as None """
            Rectangle(3, 5, 4, None)

            """ y as float """
            Rectangle(3, 5, 4, 4.4)

            """ y as infinite float """
            Rectangle(3, 5, 4, float('inf'))

            """ y as 'nan' """
            Rectangle(3, 5, 4, float('nan'))

            """ y as string """
            Rectangle(3, 5, 4, "Hey")

            """ y as List """
            Rectangle(3, 5, 4, [3, 4])

            """ y as tuple """
            Rectangle(3, 5, 4, (1,))

            """ y as dictionary """
            Rectangle(3, 5, 4, {'a': 1})

            """ y as set """
            Rectangle(3, 5, 4, {1, 2})

            """ y as set """
            Rectangle(3, 5, 4, True)

            """ y as bytes """
            Rectangle(3, 5, 4, b'Alx')

    def testInvalidYValue(self):

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):

            """ y = -ve """
            Rectangle(3, 5, 4, -1)
