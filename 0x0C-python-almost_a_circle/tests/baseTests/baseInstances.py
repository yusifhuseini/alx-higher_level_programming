#!/usr/bin/python3

"""
Test model for Base class
"""

import unittest
from models.base import Base


class BaseTestInstantiation(unittest.TestCase):

    def testWithIdNone(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def testWithoutId(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def testWithIntegerId(self):
        b1 = Base(2)
        self.assertEqual(b1.id, 2)

    def testWithFloatId(self):
        b1 = Base(5.5)
        self.assertEqual(b1.id, 5.5)

    def testWithFloatNanId(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def testWithFloatInfId(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def testWithByteId(self):
        self.assertEqual(b'DevOps', Base(b'DevOps').id)

    def testWithStringId(self):
        b1 = Base("Hello")
        self.assertEqual(b1.id, "Hello")

    def testWithListId(self):
        b1 = Base([1, 2])
        self.assertEqual(b1.id, [1, 2])

    def testWithTupleId(self):
        b1 = Base((2, 3))
        self.assertEqual(b1.id, (2, 3))

    def testWithExcessArgumenents(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def testAccessToPublicAttribute(self):
        b1 = Base(5)
        b1.id = 7
        self.assertEqual(b1.id, 7)

    def testAccesToPrivateAttribute(self):
        with self.assertRaises(AttributeError):
            b1 = Base(2)
            print(b1.__nb_objects)
