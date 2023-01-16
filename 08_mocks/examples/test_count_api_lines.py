"""Unit test to for count_api_lines"""

import unittest
import unittest.mock
import count_api_lines

"""Unit test class for count_api_lines"""
class TestCountApiLines(unittest.TestCase):

    def test_happy_path(self):
        """Test happy path"""

        with unittest.mock.patch("requests.get") as mock_get:
            mock_get.return_value = MockResponse("Line one\nLine two\nLine three")
            num_lines = count_api_lines.count_api_lines("https://google.com")
            self.assertEqual(3, num_lines)
            self.assertEqual(1, mock_get.call_count)

"""Class to simulate a real response from request.get"""
class MockResponse:
    def __init__(self, value):
        self.text = value

if __name__ == "__main__":
    unittest.main()