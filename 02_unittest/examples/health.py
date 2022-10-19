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
