#!/usr/bin/python3

"""
Test model for Base class
"""

import unittest
from tests.baseTests.baseInstances import BaseTestInstantiation as B1
from tests.baseTests.baseJson import TestJsonStringFormat as B2
from tests.baseTests.baseJson import TestSaveToJsonFile as B3
from tests.baseTests.baseJson import TestFromJsonStringToPythonList as B4
from tests.baseTests.baseCreate import TestBaseCreateMethod as B5
from tests.baseTests.baseJson import TestLoadFromJsonFile as B6
from tests.baseTests.baseCsv import TestSaveToCsvFile as B7
from tests.baseTests.baseCsv import TestLoadFromCsvFile as B8


loader = unittest.TestLoader()

b1 = loader.loadTestsFromTestCase(B1)
b2 = loader.loadTestsFromTestCase(B2)
b3 = loader.loadTestsFromTestCase(B3)
b4 = loader.loadTestsFromTestCase(B4)
b5 = loader.loadTestsFromTestCase(B5)
b6 = loader.loadTestsFromTestCase(B6)
b7 = loader.loadTestsFromTestCase(B7)
b8 = loader.loadTestsFromTestCase(B8)


suite = unittest.TestSuite([b1, b2, b3, b4, b5, b6, b7, b8])


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
