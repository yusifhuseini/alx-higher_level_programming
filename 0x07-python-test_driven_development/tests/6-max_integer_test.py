#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for 'max_integer' function
    """
    def testEmptyList(self):
        """Test an empty list"""
        result = max_integer([])
        self.assertEqual(None, result)

    def testSingleElementList(self):
        """Test for a single element"""
        result = max_integer([10])
        self.assertEqual(10, result)

    def testListOfEqualElements(self):
        """Test list of equal elements"""
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(5, result)

    def testSortedListOfIntegers(self):
        """Test an sorted list of integers"""
        result = max_integer([5, 6, 7, 8])
        self.assertEqual(8, result)

    def testReversedListOfIntegers(self):
        """Test a reversed list of integers"""
        result = max_integer([8, 7, 6, 5])
        self.assertEqual(8, result)

    def testListOfNegativeIntegers(self):
        """Test list of negative integers"""
        result = max_integer([-8, -2, -4, -11, -1])
        self.assertEqual(-1, result)

    def testListOfFloats(self):
        """Test list of floats"""
        result = max_integer([1.1, 2.2, 3.5, 0.245])
        self.assertEqual(3.5, result)

    def testListOfMixedDataTypes(self):
        """Test list of integers and float"""
        result = max_integer([-9.98, -20, 0, 7, -54])
        self.assertEqual(7, result)

    def testListsOfStrings(self):
        """Test a list of strings"""
        names = ['zaki', 'slam', 'Chillz', 'zaki']
        result = max_integer(names)
        self.assertEqual('zaki', result)


if __name__ == '__main__':
    unittest.main()
