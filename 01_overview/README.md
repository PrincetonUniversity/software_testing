# Software Testing for Computational Researchers

This workshop is designed for anyone doing computational research that writes software toward a software tool or for data analysis. It is not designed

Don't try to become a professional software tester but if you are writing code toward software projects or writing data analysis code then you should spend some time writing tests for the software you write.

In short, testing is about the actual outputs agreeing with the expected outputs.

Here is a function and a few associated tests:

```python
def f(a, b):
  return a + b

assert f(1, 2) == 3
assert f(1, -1) == 0
assert f(1, 2 + 1j) == 3 + 1j
assert f(['cat'], ['dog']) == ['cat', 'dog']
```

The above should be thought of as a pseudo-code exmaple. We will demonstrate multiple testing frameworks in this workshop.

# Reasons to write tests

#### *Mistakes are easy to make*

C/C++ allow for assignment in an if statement:

```c++
if (a = b) {
  // do work
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

By writing a test suite you will have confidence that at least all the test will run. Running the test suite is usually the first thing to do when a bug is found.

#### *Promotes writing proper code*

If you can't write tests for your code then the structure and design choices of the code are probably poor. An example is a lengthy routine that writes to STDOUT and returns nothing.

#### *A test suite makes debugging easier*

If you have a battery of tests for a certain piece of code then when a bug arises you can run the test suite to rule out potential problems.

#### *Version control is different than a test suite*

While version control provides a record of all the states of the code and the changes made, it does not help with mistakes. A test suite can be used to identify mistakes introduces in the code base.

# Terminology

Heirarchy of Tests

unit - tests written for standalone units of the code (e.g., function)

integration

system

# Practical Example

The data file is composed on x, y, z coordinates:

```
$ head -n 3 mydata.csv
2.2, 3.4, 1.9
4.0, 0.2, 3.0
1.1, 9.5, 5.4
```

The following code reads in a file 

```python
import pandas as pd

def compute_min_distance_between_all_pairs(df):
  return x - y

if __name__ == "__main__":
  df = pd.read_csv("myfile.dat")
  min_dist = compute_min_distance_between_all_pairs(df):
  print(f"The minimum distance between all pairs of points is {min_dist}")
```

Make sure you can run `circle_area.py` on Adroit or another machine:

```
$ ssh <YourNetID>@adroit.princeton.edu
$ git clone <this repo>
$ cd software_testing/01_overview
$ module load anaconda3
$ python circle_area.py
```

How can we write code to test the correctness of `compute_min_distance_between_all_pairs`? See the next section where the Python `unittest` module is discussed.

If people can't write the main code without errors then why should they be trusted to write the test code? Should there be test code for the test code?
