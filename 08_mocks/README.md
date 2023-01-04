# Unit Test Mocking

Mocking is a technique in testing to replace a function, class or attribute in the
code being tested with a mock version so your test can control what that element does.

This can be useful to:

* Create a test to verify what happens when your code calls a function that returns an error.
* Test the code in your unit without depending on functions called by your unit. You can use this to make your tests run faster by simulating the calls, but still testing the code in your unit.
* Allows test to pass even if an external dependency are not available where you run your tests.
* Allow your tests to be deterministic and pass even when dependencies return different results.

## Example 1


    file: my_func.py
    
        import requests
        
        """Send http request to URL and count lines in response."""
        def myfunc(url):
        	response = requests.get(url)
        	lines = response.text.split("\n")
        	return len(lines)
        
## Test For Example 1

We want to write a test for myfunc. However, we just want to test our code and not the URL server that it is calling. We will write the test and mock out the API call (`test_my_func.py`).

```python
import unittest
from unittest import mock
from my_func import myfunc
	
class MockResponse:
    def __init__(self, value):
        self.text = value
	
class TestMyFunc(unittest.TestCase):
    def test_happy_path(self):
        with mock.patch("requests.get") as mock_get:
            mock_get.return_value = MockResponse("L1\n L2\n L3")
            num_lines = myfunc("https://google.com")
            self.assertEqual(3, num_lines)
```

Notice the request to google.com is not actually called, but the API call is mocked out with mock.patch to return the MockResponse instead.
