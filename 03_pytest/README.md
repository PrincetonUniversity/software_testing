# pytest

[pytest](https://docs.pytest.org/en/stable/) is a framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

## Installation

`pytest` is not part of the Python standard library but it is available from the `anaconda3` modules:

```bash
$ ssh <YourNetID>@adroit.princeton.edu
$ module load anaconda3/2021.5
$ pytest --version
```

If you are not on Adroit then see the instructions [below](https://github.com/PrincetonUniversity/software_testing/tree/main/04_pytest#appendix-installation) or the [pytest webpage](https://docs.pytest.org/en/stable/getting-started.html).

## Intro

* pytest will run all files of the form `test_*.py` or `*_test.py` in the current directory and its subdirectories.
* it uses detailed assertion introspection (so need to remember self.assert* names)
* it is compatible with the `unittest` module

```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

To run the test:

```
$ cd software_testing/04_pytest
$ pytest test_sample.py
===================================== test session starts =====================================
platform linux -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /scratch/gpfs/jdh4/TESTING/04_pytest
collected 1 item                                                                              

test_sample.py F                                                                        [100%]

========================================== FAILURES ===========================================
_________________________________________ test_answer _________________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:7: AssertionError
=================================== short test summary info ===================================
FAILED test_sample.py::test_answer - assert 4 == 5
====================================== 1 failed in 0.10s ======================================
```

To run the `test_` files in the current directory you can call `pytest` without any arguments.

```bash
$ pytest                    # run all test files
$ pytest -q test_sample.py  # quiet mode
$ pytest -v test_sample.py  # verbose mode
```

## Example

Recall the `circle_area.py` module:

```python
import math

def circle_area(radius):
  if not type(radius) in [int, float]:
      raise TypeError("The radius is not an int or float.")
  if (radius < 0):
      raise ValueError("The radius cannot be negative.")
  return math.pi * radius**2
```

Here is how the test would appear for pytest:

```python
import pytest
from circle_area import circle_area
import math

class TestClass:

    def test_area(self):
        # test areas when radius >= 0
        assert circle_area(1) == math.pi
        assert circle_area(0) == 0
        assert circle_area(2.1) == math.pi * 2.1**2

    def test_values(self):
        # raise value error when radius is negative
        with pytest.raises(ValueError):
            circle_area(-2)

    def test_types(self):
        # handle type errors
        with pytest.raises(TypeError):
            circle_area(3+5j)
        with pytest.raises(TypeError):
            circle_area(True)
        with pytest.raises(TypeError):
            circle_area("cat")
```

Try out the above with:

```
$ cd software_testing/04_pytest/circle
$ pytest
```

## Compatibility with unittest

`pytest` can be used to run tests written using `unittest`:

```
$ cat software_testing/02_unittest/test_circle_area.py
$ pytest software_testing/02_unittest/test_circle_area.py
```

## Appendix: Installation

`pytest` is available on PyPI and Anaconda Cloud. You may be able to install it on your personal machine with one of these commands:

```bash
$ pip install pytest
```

```bash
$ conda install pytest
```
