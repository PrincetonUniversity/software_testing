"""software_testing/02_unittest/examples/test_shapes_print.py"""
import unittest
from shapes import Circle
import math

class TestCircle(unittest.TestCase):

    def setUp(self):
        # do setup operations here for each test
        print("setUp")
        self.c1 = Circle(3, "red")
        self.c2 = Circle(5, "green")
      
    def test_colors(self):
        print("test_colors")
        self.assertEqual(self.c1.color, "red")
        self.assertEqual(self.c2.color, "green")

        self.c1.change_color("blue")
        self.c2.change_color("blue")
        self.assertEqual(self.c1.color, "blue")
        self.assertEqual(self.c2.color, "blue")

    def test_area(self):
        print("test_area")
        self.assertAlmostEqual(self.c1.compute_area(), math.pi * 3**2)
        self.assertAlmostEqual(self.c2.compute_area(), math.pi * 5**2)

    def tearDown(self):
        # do teardown operations here for each test
        print("tearDown")

if __name__ == "__main__":
    unittest.main()
