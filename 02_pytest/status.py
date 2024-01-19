from func import func
import pytest
import flask
import requests

def test_answer():
    assert func(3) == 4
    print("Success!")

if __name__ == "__main__":
    test_answer()
