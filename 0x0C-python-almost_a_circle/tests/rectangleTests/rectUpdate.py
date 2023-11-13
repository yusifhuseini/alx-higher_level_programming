#!/usr/bin/python3

"""
A test module for Rectangle update method
"""

import unittest
from models.rectangle import Rectangle


class TestRectangleUpdateMethod(unittest.TestCase):

    def testWithoutArgs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def testWithOneArgs(self):
        r = Rectangle(1, 1)
        r.update(2)
        self.assertEqual(r.id, 2)

    def testWithIdNone(self):
        r = Rectangle(1, 1)
        r.update(None)
        self.assertEqual("[Rectangle] ({}) 0/0 - 1/1".format(r.id), str(r))

    def testWithTwoArgs(self):
        r = Rectangle(1, 1)
        r.update(2, 3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)

    def testWithThreeArgs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def testWithFourArgs(self):
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def testWithFiveArgs(self):
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def testWithAboveFiveArgs(self):
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6, 7)
        self.assertEqual("[Rectangle] (2) 5/6 - 3/4", str(r))

    def testWithIdNoneAndMoreArgs(self):
        r = Rectangle(1, 1)
        r.update(None, 3, 4, 5)
        self.assertEqual("[Rectangle] ({}) 5/0 - 3/4".format(r.id), str(r))

    def testWithInvalidWidth(self):
        r = Rectangle(1, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(2, "")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, 0)
            r.update(2, -1)

    def testWithInvalidHeight(self):
        r = Rectangle(1, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 3, "")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(2, 3, 0)
            r.update(2, 3, -1)

    def testWithInvalidX(self):
        r = Rectangle(1, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 3, 4, "")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(2, 3, 4, -1)

    def testWithInvalidY(self):
        r = Rectangle(1, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(2, 3, 4, 5, "")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(2, 3, 4, 5, -1)

    def testInvalidWithAndHeight(self):
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(2, "", 4, -1)

    def testInvalidHeightAndX(self):
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 3, "", -1)

    def testInvalidXandY(self):
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 3, 4, "", "")

    """ Kwargs tests """
    def testWithOneKwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2)
        self.assertEqual(r.id, 2)

    def testWithTwoKwargs(self):
        r = Rectangle(1, 1, 1, 1)
        r.update(id=2, width=3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)

    def testWithThreeKwargs(self):
        r = Rectangle(1, 1, 1, 1)
        r.update(id=2, width=3, height=4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def testWithFourKwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2, width=3, height=4, x=5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def testWithFiveKwargs(self):
        r = Rectangle(1, 1, 1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def testWithoutKwargsOrder(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(x=2, height=3, id=4, y=5, width=6)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 5)

    def testWithKwargsIdAsNone(self):
        r = Rectangle(1, 2, 2, 1)
        r.update(id=None)
        self.assertEqual("[Rectangle] ({}) 2/1 - 1/2".format(r.id), str(r))

    def testWithKwargsIdAsNoneAndMore(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(x=2, height=3, id=None, y=5, width=6)
        self.assertEqual("[Rectangle] ({}) 2/5 - 6/3".format(r.id), str(r))

    def testWithInvalidKeyInKwargs(self):
        r = Rectangle(1, 1, 1, 1)
        r.update(z=9, id=2, i=11)
        self.assertEqual(r.id, 2)
        with self.assertRaises(AttributeError):
            z = r.z
            i = r.i

    def testWithInvalidWidth(self):
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
            r.update(width=-1)

    def testWithInvalidHeight(self):
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
            r.update(height=-1)

    def testWithInvalidX(self):
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)

    def testWithInvalidY(self):
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-1)

    def testWithNonEmptyArgsAndKwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, id=4, width=5, height=6, x=7, y=8)
        self.assertEqual("[Rectangle] (2) 1/1 - 3/1", str(r))
