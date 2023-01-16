"""Unit test to test count_loc"""

import count_loc
import pytest
import os

def test_happy_path():
    count_loc.GPFS_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "mock_data")
    num_lines = count_loc.count_loc()
    assert 4 == num_lines

if __name__ == "__main__":
    pytest.main([__file__])