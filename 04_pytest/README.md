# pytest

[pytest](https://docs.pytest.org/en/stable/) is a framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

## Installation

`pytest` is not part of the standard library so you will need to install it. It is available on PyPI and Anaconda Cloud via the conda-forge channel.

* pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.
* detailed info on failing assert statements (no need to remember self.assert* names)

```python
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

To run the test:

```
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

```
$ cd software_testing/04_pytest/01_hello_world
$ pytest
$ pytest -q test_sample.py
$ pytest -v test_sample.py
```
