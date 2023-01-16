"""software_testing/08_mocks/examples/count_api_lines.py"""
import requests

"""Send http request to URL and count lines in response."""
def count_api_lines(url):
    response = requests.get(url)
    lines = response.text.split("\n")
    return len(lines)
