import math

class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def compute_area(self):
        return math.pi * self.radius**2

    def change_color(self, new_color):
        self.color = new_color
