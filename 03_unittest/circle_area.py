"""software_testing/02_unittest/circle_area.py"""
import math

def circle_area(radius):
    if not type(radius) in (int, float):
        raise TypeError("The radius is not an int or float.")
    if radius < 0:
        raise ValueError("The radius cannot be negative.")    
    return math.pi * radius**2
  
if __name__ == "__main__":
    radius_values = [2, 0, -3, 2 + 5j, True, "cat"]
    for radius in radius_values:
        area = circle_area(radius)
        print(f"Area of circle with radius = {radius} is {area}")
