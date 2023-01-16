"""software_testing/02_unittest/test_circle_area.py"""
import unittest
from circle_area import circle_area
import math

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), math.pi * 2.1**2)

if __name__ == "__main__":
    unittest.main()
