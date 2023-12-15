# pytest

The [pytest](https://docs.pytest.org/en/stable/) package is an alternative to unittest. You create tests with functions instead of classes and you typically just use standard python assert methods. 

You use the pytest command line tool to execute tests. The pytest command line tools can be used to execute tests created with either unittest or pytest so you can write unit tests with either test framework.

The pytest package is not part of the standard python library so it needs to be installed with PIP or loaded with a module on adroit. See the appendix at end of this file.


## Example Test with PyTest

Assume a source code file (`func.py`).

```
def func(x):
	return x + 1
```

Then a test case for that file in pytest could be (`test_func.py`).

```
from func import func

def test_func():
	assert func(3) == 4
```
This does the same thing as a unit test written with the unittest package, but it is less code without classes.

## Running PyTest Unit Test
You can execute the unit test using pytest.

```
pytest test_func.py

collected 1 item
test_func.py .                      [100%]
```


To run the `test_` files in the current directory you can call `pytest` without any arguments. This will run all tests in the current directory and all sub-directires so you can execute a full test suite.

The following arguments to pytest are useful.

```bash
$ pytest                    # run all test files
$ pytest -q test_sample.py  # quiet mode
$ pytest -v test_sample.py  # verbose mode
$ pytest -s test_sample.py  # show print messages in code or tests
```

Without the -s option print statements in your code do nothing. Use -s to see print statements.

If you add these lines to the test case file:

```
if __name__ == "__main__":
	import pytest
	pytest.main([__file__])
```

Then you can also execute the test with:

```python test_func2.py```

## Test Fixtures

Unit tests often need to set up and tear down the test environment between each test. In the unittest package this is done with setUp() and tearDown() methods. With pytest this is done with fixtures.

A test fixture is defined by a function with a @pytest.fixture() annotation. A single function contains both the set up and tear down code seperated by a yield statement. 


```python
import pytest
from func import func

@pytest.fixture(autuse=True)
def setUp():
	print()
	print("setUp")
	yield
	print("tearDown")

def test_answer():
    print("Run Test")
    assert func(3) == 4
```

You may have multiple fixtures in the same test file.

Run the example above with the -s option to see the print statement messages

```bash
pytest -s test_with_fixture.py
test_with_fixture.py 
setUp
Run Test
.tearDown
```

See the examples folder for exercise files.

## Exercise 1

Consider a function that finds people based on zipcode by looking in a large demographics file in our project GPFS file system. The function is in (`find_people.py`).

```python
import csv

"""Folder in our large project GPFS file system"""
GPFS_FOLDER = "/myproject_data"

def find_people(search_zip_code):
    """Find people that live in a specific zip code and return their demographic information"""

    result = []
    demographics_csv = f"{GPFS_FOLDER}/private_info/demographics.csv"
    with open(demographics_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            zip_code = row[3]
            if zip_code == search_zip_code:
                result.append(row)
    return result
```

We could write a unit test that calls `find_people` with a zipcode and checks the number of people returned. However, this test case would only work if we run it on our project machine that contain the /myproject_data GPFS. Also, the GPFS data changes often so our test case may pass today, but then fail tomorrow because the data changes.

There are many ways to address this issue, but one way is to have the test case generate test data and simulate the contents of the GPFS. Fixtures are a good way to set up and tear down this test data.

Consider the following test written in pytest (`test_find_people.py`).

```python
import pytest
import find_people
import mock_data

@pytest.fixture(autouse=True)
def setUp():
    mock_dir = mock_data.generate_test_data()
    find_people.GPFS_FOLDER = mock_dir
    yield
    mock_data.delete_temp_directory(mock_dir)

def test_legal_zipcode():
    people = find_people.find_people("10036")
    assert len(people) == 1

def test_multiple_results():
    people = find_people.find_people("10019")
    assert len(people) == 2

def test_no_results():
    people = find_people.find_people("00000")
    assert len(people) == 0

```

This test case calls a function in our test directory to mock up the test data and then replace the contents of the `find_people.GPFS_FOLDER` variable before finding people. After the test it deletes our test data to clean up.

This test run fast because the test data is small and we can control the test data and simulate any test scenario we want.

## Appendix: Installation

`pytest` is available on PyPI and Anaconda Cloud. You may be able to install it on your personal machine with one of these commands:

```bash
$ pip install pytest
```

```bash
$ conda install pytest
```

```bash
$ ssh <YourNetID>@adroit.princeton.edu
$ module load anaconda3/2022.5
$ pytest --version
