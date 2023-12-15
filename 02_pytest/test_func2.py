
from func import func

def test_answer():
    assert func(3) == 4

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
