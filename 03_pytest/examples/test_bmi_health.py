"""software_testing/03_unittest/examples/test_bmi_health.py"""
import pytest
from bmi_health import BMI, to_kg, to_meters

@pytest.fixture()
def bmi_1():
    # Setup BMI 1
    yield BMI(10.0, 1.0)
    # Teardown BMI 1
    pass

@pytest.fixture()
def bmi_2():
    bmi = BMI(1, 1)
    bmi.set_name("Charlie")
    return bmi

@pytest.fixture()
def bmi_3():
    return BMI(to_kg(170), to_meters(5, 10))

def test_mass_height(bmi_1, bmi_2):
    assert(bmi_1.mass == 10.0)
    assert(bmi_1.height == 1)
    assert(bmi_2.name == "Charlie")

def test_bmi(bmi_1, bmi_2, bmi_3):
    assert(bmi_1.compute_bmi() == 10)
    assert(bmi_2.compute_bmi() == 1)
    assert(round(bmi_3.compute_bmi(), 2) == 24.39)

if __name__ == "__main__":
    pytest.main([__file__])