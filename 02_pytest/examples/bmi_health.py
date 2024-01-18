"""software_testing/02_pytest/examples/bmi_health.py"""
class BMI:
    """Class to compute body mass index."""

    def __init__(self, mass:float, height:float)->float:
        """Constructor."""
        self.mass = mass
        self.height = height
        self.name = ""

    def compute_bmi(self):
        """Compute BMI of mass, height from constructor"""
        return self.mass / self.height**2

    def set_name(self, new_name):
        """Set the name of the person with the BMI."""
        self.name = new_name

    def is_overweight(self):
        """Returns True if the person is overweight."""
        return self.compute_bmi() > 25

def to_kg(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.453592

def to_meters(feet, inches):
    """Convert feet/inches to meters."""
    return (feet * 12 + inches) * 0.0254