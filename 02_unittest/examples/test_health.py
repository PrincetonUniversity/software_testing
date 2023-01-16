"""software_testing/02_unittest/examples/test_health.py"""
import unittest
from health import BMI, to_kg, to_meters

class TestBMI(unittest.TestCase):

    def setUp(self):
        """do setup operations here for each scenario"""
        self.b1 = BMI(10.0, 1.0)
        self.b2 = BMI(1, 1)
        self.b2.set_name("Charlie")
        self.b3 = BMI(to_kg(170), to_meters(5, 10))
        self.b4 = BMI(to_kg(200), to_meters(5, 10))
        
    def test_mass_height(self):
        """Validate mass, height and names for the scenarios."""
        self.assertEqual("", self.b1.name)
        self.assertEqual(10.0, self.b1.mass)
        self.assertEqual(1, self.b1.height)
        self.assertEqual("Charlie", self.b2.name)
        self.assertEqual(1, self.b2.mass)
        self.assertEqual(77, round(self.b3.mass))

    def test_bmi(self):
        """Validate BMI for the scenarios."""
        self.assertEqual(10, self.b1.compute_bmi())
        self.assertEqual(1, self.b2.compute_bmi())
        self.assertEqual(24.39, round(self.b3.compute_bmi(), 2))
        self.assertEqual(28.7, round(self.b4.compute_bmi(), 2), 28.7)

    def test_overweight(self):
        """Validate overweight computation for the scenarios."""
        self.assertEqual(False, self.b3.is_overweight(), "Expected b3 not overweight")
        self.assertEqual(True, self.b4.is_overweight(), "Expected b3 overweight")

    def tearDown(self):
        """do teardown operations here for each scenario. Nothing to do."""
        pass
    
if __name__ == "__main__":
    unittest.main()
