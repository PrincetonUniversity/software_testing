"""software_testing/08_mocks/examples/test_count_loc.py"""

import os
import unittest
import count_loc

"""Unit test class for myfunc tests"""
class TestCountLoc(unittest.TestCase):
    
    """Test happy path"""
    def test_happy_path(self):
        count_loc.GPFS_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "mock_data")
        num_lines = count_loc.count_loc()
        self.assertEqual(4, num_lines)

if __name__ == "__main__":
    unittest.main()