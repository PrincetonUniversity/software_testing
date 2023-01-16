import pytest
import count_api_lines

def test_happy_path(mocker):
    """Test count_api_lines using mocked value of API call."""

    mocker.patch("requests.get", return_value=MockResponse("Line one\nLine two\nLine three"))
    num_lines = count_api_lines.count_api_lines("https://google.com")
    assert num_lines==3

"""Class to simulate a response from request.get"""
class MockResponse:
    def __init__(self, value):
        self.text = value

if __name__ == "__main__":
    pytest.main([__file__])