import unittest
from health import BMI

class TestBMI(unittest.TestCase):

    def setUp(self):
        # do setup operations here for each test
        self.b1 = BMI(10.0, 1.0)
        self.b2 = BMI(1, 1)
        
    def test_props(self):
        self.assertEqual(self.b1.mass, 10.0)
        self.assertEqual(self.b1.height, 1)

        self.assertEqual(self.b2.name, "")
        self.b2.set_name("Charlie")
        self.assertEqual(self.b2.name, "Charlie")

    def test_bmi(self):
        self.assertAlmostEqual(self.b1.compute_bmi(), 10)
        self.assertAlmostEqual(self.b2.compute_bmi(), 1)

    def tearDown(self):
        # do teardown operations here for each test
        pass
    
if __name__ == "__main__":
    unittest.main()
