#!/usr/bin/python3

"""
Test model for Base class
"""

import unittest
from tests.squareTests.squareInstances import TestSquareInstantiation as S10
from tests.squareTests.squareAttributes import TestSquareSize as S20
from tests.squareTests.squareAttributes import TestSquareX as S21
from tests.squareTests.squareAttributes import TestSquareY as S22
from tests.squareTests.squareArea import TestMethodSquareArea as S23
from tests.squareTests.squareDisplay import TestSquareDisplay as S24
from tests.squareTests.squareDisplay import TestSquareString as S25
from tests.squareTests.squareUpdate import TestSquareUpdateMethod as S26
from tests.squareTests.squareDisplay import TestSquareDictionary as S27

TestLoader = unittest.TestLoader()

s1 = TestLoader.loadTestsFromTestCase(S10)
s2 = TestLoader.loadTestsFromTestCase(S20)
s3 = TestLoader.loadTestsFromTestCase(S21)
s4 = TestLoader.loadTestsFromTestCase(S22)
s5 = TestLoader.loadTestsFromTestCase(S23)
s6 = TestLoader.loadTestsFromTestCase(S24)
s7 = TestLoader.loadTestsFromTestCase(S25)
s8 = TestLoader.loadTestsFromTestCase(S26)
s9 = TestLoader.loadTestsFromTestCase(S27)

suite = unittest.TestSuite([s1, s2, s3, s4, s5, s6, s7, s8, s9])


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
