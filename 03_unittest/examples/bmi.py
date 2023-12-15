"""software_testing/02_unittest/examples/bmi.py"""

def bmi(mass, height):
    if not type(mass) in (int, float):
        raise TypeError("The mass is not an int or float.")
    if not type(height) in (int, float):
        raise TypeError("The height is not an int or float.")
    if mass < 0:
        raise ValueError("The mass cannot be negative.")   
    if height < 0:
        raise ValueError("The height cannot be negative.")   
    if height == 0:
        raise ZeroDivisionError("The height cannot be zero.")   
    return mass / height**2
  
