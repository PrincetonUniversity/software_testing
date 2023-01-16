class BMI:

    def __init__(self, mass, height):
        self.mass = mass
        self.height = height
        self.name = ""

    def compute_bmi(self):
        # tests removed for brevity
        return self.mass / self.height**2

    def set_name(self, new_name):
        self.name = new_name

    def is_overweight(self):
        return self.compute_bmi() > 25

def to_kg(pounds):
    return pounds * 0.453592

def to_meters(feet, inches):
    return (feet * 12 + inches) * 0.0254