import pytest
from bmi_health import BMI

@pytest.fixture()
def bmi_1():
    # Setup BMI 1
    yield BMI(10.0, 1.0)
    # Teardown BMI 1
    pass

@pytest.fixture()
def bmi_2():
    return BMI(1, 1)

def test_props(bmi_1, bmi_2):
    assert(bmi_1.mass == 10.0)
    assert(bmi_1.height == 1)

    assert(bmi_2.name == "")
    bmi_2.set_name("Charlie")
    assert(bmi_2.name == "Charlie")

def test_bmi(bmi_1, bmi_2):
    assert(bmi_1.compute_bmi() == 10)
    assert(bmi_2.compute_bmi() == 1)

if __name__ == "__main__":
    pytest.main()