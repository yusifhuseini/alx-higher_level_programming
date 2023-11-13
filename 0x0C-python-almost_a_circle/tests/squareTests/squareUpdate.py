#!/usr/bin/python3

"""
A test module for Rectangle update method
"""

import unittest
from models.square import Square


class TestSquareUpdateMethod(unittest.TestCase):

    def testWithoutArgs(self):
        s = Square(3, 1, 2, 3)
        s.update()
        self.assertEqual("[Square] (3) 1/2 - 3", str(s))

    def testWithOneArgs(self):
        s = Square(3)
        s.update(2)
        self.assertEqual(s.id, 2)

    def testWithIdNone(self):
        s = Square(3)
        s.update(None)
        self.assertEqual("[Square] ({}) 0/0 - 3".format(s.id), str(s))

    def testWithTwoArgs(self):
        s = Square(3)
        s.update(2, 3)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)

    def testWithThreeArgs(self):
        s = Square(2, 2, 2, 2)
        s.update(2, 3, 4)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)

    def testWithFourArgs(self):
        s = Square(2)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def testWithIdNoneAndMoreArgs(self):
        s = Square(2)
        s.update(None, 3, 4, 5)
        self.assertEqual("[Square] ({}) 4/5 - 3".format(s.id), str(s))

    def testWithInvalidSize(self):
        s = Square(2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(2, "")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(2, 0)
            s.update(2, -1)

    def testWithInvalidX(self):
        s = Square(3)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 3, "")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(2, 3, -1)

    def testWithInvalidY(self):
        s = Square(2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(2, 3, 4, "")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(2, 3, 4, -1)

    def testInvalidSizeAndX(self):
        s = Square(2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(2, "", -1)

    def testInvalidXAndY(self):
        s = Square(2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 3, "", -1)

    """ Kwargs tests """
    def testWithOneKwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2)
        self.assertEqual(s.id, 2)

    def testWithTwoKwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2, size=3)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)

    def testWithThreeKwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2, size=3, x=4)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)

    def testWithFourKwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2, size=3, x=4, y=5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def testWithoutKwargsOrder(self):
        s = Square(1, 1, 1, 1)
        s.update(x=2, id=4, y=5, size=6)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 5)

    def testWithKwargsIdAsNone(self):
        s = Square(1, 2, 2, 1)
        s.update(id=None)
        self.assertEqual("[Square] ({}) 2/2 - 1".format(s.id), str(s))

    def testWithKwargsIdAsNoneAndMore(self):
        s = Square(5, 5, 5, 5)
        s.update(x=2, id=None, y=5, size=6)
        self.assertEqual("[Square] ({}) 2/5 - 6".format(s.id), str(s))

    def testWithInvalidKeyInKwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(z=9, id=2, i=11)
        self.assertEqual(s.id, 2)
        with self.assertRaises(AttributeError):
            z = s.z
            i = s.i

    def testWithInvalidSize(self):
        s = Square(1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)
            s.update(size=-1)

    def testWithInvalidX(self):
        s = Square(1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-1)

    def testWithInvalidY(self):
        s = Square(1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-1)

    def testWithNonEmptyArgsAndKwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(2, 3, id=4, size=5, x=7, y=8)
        self.assertEqual("[Square] (2) 1/1 - 3", str(s))
