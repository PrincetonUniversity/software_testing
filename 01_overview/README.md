# Software Testing for Computational Researchers

This workshop is for computational researchers who write data analysis scripts, software tools or software packages. Our message in short is that you if you are writing code toward software projects or writing data analysis scripts then you should spend some time writing tests for the software you write.

Here is a simple function and a few associated tests:

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

C/C++ allows for assignment in an if statement:

```c++
if (a = b) {
  //  block of code to be executed if the condition is true
}
```

Changes made between Python 2 and 3

```python
a = 1
b = 2
a / b  # equals 0 in Python 2
a / b  # equals 0.5 in Python 3
```

#### *Inspire confidence*

If your test suite executes successfully then you will have more confidence in your code.

#### *Promotes writing proper code*

If you can't write tests for your code then the structure and design choices of the code are probably poor.

#### *A test suite makes debugging easier*

If you have a battery of tests for a certain piece of code then when a bug arises you can run the test suite to rule out potential problems. Running the test suite is usually the first thing to do when a bug is found.

#### *Version control is different than a test suite*

While version control provides a record of all the states of the code and the changes made, it does not help with mistakes. A test suite can be used to identify mistakes in the codebase.

## Terminology

Test should be written to span a hierarchy of scales:

* unit tests cover elementary units of code such as a simple function
* integration tests cover collections of elementary units and modules (looking for problems with how the pieces interact)
* system tests cover the entire application

## Questions

If people are unable to write the main code without errors then why should they be trusted to write the test code? Should there be test code for the test code?
