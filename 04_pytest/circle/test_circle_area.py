import pytest
from circle_area import circle_area
import math

class TestClass:

    def test_area(self):
        # test areas when radius >= 0
        assert circle_area(1) == math.pi
        assert circle_area(0) == 0
        assert circle_area(2.1) == math.pi * 2.1**2

    def test_values(self):
        # raise value error when radius is negative
        with pytest.raises(ValueError):
            circle_area(-2)

    def test_types(self):
        # handle type errors
        with pytest.raises(TypeError):
            circle_area(3+5j)
        with pytest.raises(TypeError):
            circle_area(True)
        with pytest.raises(TypeError):
            circle_area("cat")
