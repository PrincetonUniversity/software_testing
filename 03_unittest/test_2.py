import unittest
from circle_area import circle_area

class TestCircleArea(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, circle_area(0))
        self.assertEqual(3.14, round(circle_area(1), 2))

if __name__ == "__main__":
    unittest.main()