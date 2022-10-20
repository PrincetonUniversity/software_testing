import unittest
from bmi import bmi

class TestBMI(unittest.TestCase):

    def test_area(self):
        # test bmi for simple inputs
        self.assertAlmostEqual(bmi(1, 1), 1)
        self.assertAlmostEqual(bmi(10, 1), 10)

    def test_values(self):
        # raise value error when mass or height is negative
        self.assertRaises(ValueError, bmi, -2, 1)
        self.assertRaises(ValueError, bmi, 1, -2)

    def test_types(self):
        # handle type errors
        self.assertRaises(TypeError, bmi, 3+5j, 1)
        self.assertRaises(TypeError, bmi, True, False)
        self.assertRaises(TypeError, bmi, "cat", "dog")
        self.assertRaises(TypeError, bmi, None, "dog")

    def test_zero(self):
        # division by zero
        self.assertRaises(ZeroDivisionError, bmi, 1, 0)

    def test_mass_illegal_type(self):
        try:
            bmi(1, "cat")
            raise AssertionError("Expected Type Error for mass")
        except Exception as e:
            self.assertEqual(type(e), TypeError)        

if __name__ == "__main__":
    unittest.main()
