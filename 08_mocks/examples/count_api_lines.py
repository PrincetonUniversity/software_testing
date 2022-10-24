import requests

"""Send http request to URL and count lines in response."""
def count_api_lines(url):
    response = requests.get(url)
    lines = response.text.split("\n")
    return len(lines)
