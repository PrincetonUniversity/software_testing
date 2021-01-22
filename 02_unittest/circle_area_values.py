import math

def circle_area(radius):
  return math.pi * radius**2

radius_values = [2, 0, -3, 2 + 5j, True, "cat"]
for radius in radius_values:
  area = circle_area(radius)
  print(f"Area of circle with radius = {radius} is {area}")
