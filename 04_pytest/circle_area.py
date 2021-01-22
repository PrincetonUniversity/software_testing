import math

def circle_area(radius):
  if (radius < 0):
      raise ValueError("The radius cannot be negative.")
  if not type(radius) in [int, float]:
      raise TypeError("The radius is not an int or float.")
  return math.pi * radius**2
