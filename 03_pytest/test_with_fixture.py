import pytest
from func import func

@pytest.fixture(autouse=True)
def setUp():
	print()
	print("setUp")
	yield
	print("tearDown")

def test_answer():
    print("Run Test")
    assert func(3) == 4
