# Software Testing for Computational Researchers

This workshop is for computational researchers who write data analysis scripts, software tools or software packages. Our message, in short, is that if you are writing code toward software projects or writing data analysis scripts then you should spend some time writing tests for the software.

Here is a simple function in python and a few associated tests:

```python
def f(a, b):
  return a + b

assert f(1, 2) == 3
assert f(1, -1) == 0
assert f(1, 2 + 1j) == 3 + 1j
assert f(['cat'], ['dog']) == ['cat', 'dog']
```

The above should be thought of as a pseudo-code example. We will demonstrate multiple testing frameworks in the coming sections.

## Reasons to write tests

#### *Mistakes are easy to make*


    def divide(x, y):
        x/y
        
    if divide(4,2) != 2:
        print("wrong")
        
This is wrong. The function was missing a return statement.

Code may be not portable. For example differences between Python 2 and 3

```python
a = 1
b = 2
a / b  # equals 0 in Python 2
a / b  # equals 0.5 in Python 3
```

#### *Inspire confidence*

If your test suite executes successfully then you will have more confidence in your code.

#### *Promotes writing proper code*

If you can't write tests for your code then the structure and design choices of the code may be poor.

#### *A test suite makes debugging easier*

If you have a battery of tests for a certain piece of code then when a bug arises (or is suspected) you can run the test suite to rule out potential problems. Running the test suite is usually the first thing to do when a bug is found.

See Wintersession [debugging workshop](https://my.princeton.edu/OWCE/rsvp?id=1340958) on January 14, 2022.


## Terminology

Your code can be tested with different types of tests:

* **unit tests** cover single units of code such as a single function or module.
* **integration tests** cover collections of units and modules (looking for problems with how the pieces interact).
* **system tests** cover the entire application.
* **regression tests** Are automated suites of tests that can be run repeatably to check for new errors introduced by new changes (often are unit tests).

## Questions

* What are examples of a testing unit?
* Do complete unit tests mean there are no bugs in the code?
* Does writng test cases slow down development?
* Should there be test code for test code?
* What does it mean when a test fails?
* Can tests improve you code design?
* What can it mean to setup up the environment for a test?
* What can it mean when it is difficult to write tests?
