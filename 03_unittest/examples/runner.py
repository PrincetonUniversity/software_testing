"""software_testing/02_unittest/examples/runner.py"""
import unittest
import test_shapes
import test_sizes

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_shapes))
suite.addTests(loader.loadTestsFromModule(test_sizes))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
