"""software_testing/02_pytest/examples/geometric_area.py"""
import math


def circle_area(radius):
    """
    Calcluate the area of a circle with the given radius.
    Raises:
        TypeError:  if the radius is an illegal type.
        ValueError: if the radius is invalid for a circle.
    """
    if not type(radius) in [int, float]:
        raise TypeError("The radius is not an int or float.")
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * radius**2
