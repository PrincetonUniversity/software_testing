"""Unit test to test MyFunc"""

import unittest
from unittest import mock
from my_func import myfunc

"""Class to simulate a real response from request.get"""
class MockResponse:
    def __init__(self, value):
        self.text = value

"""Unit test class for myfunc tests"""
class TestMyFunc(unittest.TestCase):
    """Test happy path"""
    def test_happy_path(self):
        with mock.patch("requests.get") as mock_get:
            mock_get.return_value = MockResponse("Line one\nLine two\nLine three")
            num_lines = myfunc("https://google.com")
            self.assertEqual(3, num_lines)

if __name__ == "__main__":
    unittest.main()