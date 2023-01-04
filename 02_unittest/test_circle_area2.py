import unittest
from circle_area import circle_area
import math

class TestCircleArea2(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), math.pi * 2.1**2)

    def test_values(self):
        with self.assertRaises(ValueError):
            circle_area(-2)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "cat")
        self.assertRaises(TypeError, circle_area, 3+5j)

if __name__ == "__main__":
    unittest.main()
