#!/usr/bin/python3

"""
Test model for Base class
"""

import unittest
from tests.rectangleTests.rectInstances import TestRectangleInstantiation
from tests.rectangleTests.rectAttributes import TestRectangleWidth as R20
from tests.rectangleTests.rectAttributes import TestRectangleHeight as R21
from tests.rectangleTests.rectAttributes import TestRectangleX as R22
from tests.rectangleTests.rectAttributes import TestRectangleY as R23
from tests.rectangleTests.rectArea import TestMethodRectangleArea as R24
from tests.rectangleTests.rectDisplay import TestRectangleDisplay as R25
from tests.rectangleTests.rectDisplay import TestRectangleString as R26
from tests.rectangleTests.rectUpdate import TestRectangleUpdateMethod as R27
from tests.rectangleTests.rectDisplay import TestRectangleDictionary as R28

R10 = TestRectangleInstantiation

TestLoader = unittest.TestLoader()

s1 = TestLoader.loadTestsFromTestCase(R10)
s2 = TestLoader.loadTestsFromTestCase(R20)
s3 = TestLoader.loadTestsFromTestCase(R21)
s4 = TestLoader.loadTestsFromTestCase(R22)
s5 = TestLoader.loadTestsFromTestCase(R23)
s6 = TestLoader.loadTestsFromTestCase(R24)
s7 = TestLoader.loadTestsFromTestCase(R25)
s8 = TestLoader.loadTestsFromTestCase(R26)
s9 = TestLoader.loadTestsFromTestCase(R27)
s10 = TestLoader.loadTestsFromTestCase(R28)

suite = unittest.TestSuite([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10])


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
