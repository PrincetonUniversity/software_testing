# Unit Testing with unittest

Unit testing involves writing tests for standalone units of code such as a function. You could write your own testing framework maybe
using the `assert` statement but it is better to use a framework that already exists.

### Validation vs. Verification

Verification involves not executing the code whereas validation does.


## unittest from the Python Standard Library

A good starting point for unit testing is the the [`unittest`](https://docs.python.org/3/library/unittest.html) module of the Python Standard Library. If you have Python installed then you have
this module.

```
$ module load anaconda3
$ python
>>> import unittest
```

The idea is to write code in a separate file that 

Note: It is common to feel like you are making up tests that will obviously work and don't see the point in doing. In this case remind yourself that characters do getting entered into code accidentally ("sneezing" or a developer working on little sleep, someone changes the source code for debugging) so continue writing these tests with in mind. Imagination plays an important role here but don't get carried away. You can always add more tests later.

Terminology: White box testing is when you write tests for code that you can see.

# Example

Consider a simple implemenation of a function to compute the area of a circle (`circle_area.py)`:

```python
import math

def circle_area(radius):
  return math.pi * radius**2
```

Let's test this script against different input values for radius (based on this Socratica [video](https://www.youtube.com/watch?v=1Lfv5tUGsn8)):

```python
import math

def circle_area(radius):
  return math.pi * radius**2

radius_values = [2, 0, -3, 2 + 5j, True, "cat"]
for radius in radius_values:
  area = circle_area(radius)
  print(f"Area of circle with radius={radius} is {area}")
```

Run the script above with these commands:

```
$ cd software_testing/02_unittest
$ python area.py
Area of circle with radius=2 is 12.566370614359172
Area of circle with radius=0 is 0.0
Area of circle with radius=-3 is 28.274333882308138
Area of circle with radius=(2+5j) is (-65.97344572538566+62.83185307179586j)
Area of circle with radius=True is 3.141592653589793
Traceback (most recent call last):
  File "area.py", line 8, in <module>
    area = circle_area(radius)
  File "area.py", line 4, in circle_area
    return math.pi * radius**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

The function produces nonsensical output for the last four inputs. Note that if someone accidentally used `True` as an input the code would not fail. Can we improve on our function to make it more robust? Let's also write a series of tests to make sure the mistakes highlighted in the example above are caught by the program.

## Your first unit tests

The tests will be stored in a separate file. Create the file for the unit tests with the filename `test_circle_area.py`. It is conventional to prepend `test_` to the name of the original source file. Here are the contents of `test_circle_area.py`:

```python
import unittest
from circle_area import circle_area
import math

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), math.pi * 2.1**2)
```

One can see that we wrote a class that derives from `unittest.TestCase`. We then write three simple unit tests to check cases where the radius value is greater than or equal to zero. Your test must begin with `test_`. Unit tests will be ignored if they don't follow that convention, which is good if you need a helper method for one of the test functions.

For all the different assert methods see the documentation. Here are the [most popular](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug) methods.

Note that this is an example of white box testing where we can inspect the code that we are writing the tests for. Black box testing is when tests are written when the code is not available. Test-driven development is an example of black box testing since the tests are written before the code is written.

We now have two files:

```
circle_area.py
test_circle_area.py
```

To run the tests:

```
$ python -m unittest test_circle_area.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

The `.` in the first line of output implies success of one test. While there are three assert methods, these are regarded as a single test.


Add the `-v` flag for verbose output:

```
$ python -m unittest test_circle_area.py -v
```

Return to the source code (`circle_area.py`) and handle the case of a negative area:

```python
def circle_area(radius):
    if radius < 0:
        raise ValueError("The radius cannot be negative.")   
    return math.pi * radius**2
```

Let's add an additional test to handle erroneous values:

```python
import unittest
from circle_area import circle_area
import math

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), math.pi * 2.1**2)
        
    def test_values(self):
        # raise value error when radius is negative
        self.assertRaises(ValueError, circle_area, -2)
```

You could also write the new test as:

```python
    def test_values(self):
        # raise value error when radius is negative
        with self.assertRaises(ValueError):
            circle_area(-2)
```

Once again run the tests:

```
$ python -m unittest test_circle_area.py -v
test_area (test_circle_area.TestCircleArea) ... ok
test_values (test_circle_area.TestCircleArea) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Lastly, let's handle type errors such as complex numbers and booleans:

```python
import unittest
from circle_area import circle_area
import math

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), math.pi * 2.1**2)
        
    def test_values(self):
        # raise value error when radius is negative
        self.assertRaises(ValueError, circle_area, -2)
        
    def test_types(self):
        # handle type errors
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "cat")
```

Run the unittests:

```
$ python -m unittest test_circle_area.py -v
test_area (test_circle_area.TestCircleArea) ... ok
test_types (test_circle_area.TestCircleArea) ... FAIL
test_values (test_circle_area.TestCircleArea) ... ok

======================================================================
FAIL: test_types (test_circle_area.TestCircleArea)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/scratch/gpfs/jdh4/TESTING/test_circle_area.py", line 19, in test_types
    self.assertRaises(TypeError, circle_area, True)
AssertionError: TypeError not raised by circle_area

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

We see that there is a failure. Let's modify our source code so that the tests succeed:

```python
def circle_area(radius):
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    if not type(radius) in [int, float]:
        raise TypeError("The radius is not an int or float.")
    return math.pi * radius**2
```

Now run the unit tests:

```
$ python -m unittest test_circle_area.py -v
test_area (test_circle_area.TestCircleArea) ... ok
test_types (test_circle_area.TestCircleArea) ... ok
test_values (test_circle_area.TestCircleArea) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

We see all the tests pass. Our source has been much improved.

## Exercise

Create a file called `circle_radius.py` that defines a function `circle_radius` that returns the radius of a circle given the area. Then create a second file called `test_circle_radius.py` for the unittests.

If you finish early then start writing unit tests for the scripts for your research work.

## setUp() and tearDown()

This section will illustrate the idea of `setUp()` and `tearDown()` operations. Consider the following class:

```python
import math

class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def compute_area(self):
        return math.pi * self.radius**2

    def change_color(self, new_color):
        self.color = new_color
```

You might naively begin with unit tests like the following:

```python
import unittest
from shapes import Circle
import math

class TestCircle(unittest.TestCase):

    def test_colors(self):
        c1 = Circle(3, "red")
        c2 = Circle(5, "green")

        self.assertEqual(c1.color, "red")
        self.assertEqual(c2.color, "green")

        c1.change_color("blue")
        c2.change_color("blue")
        self.assertEqual(c1.color, "blue")
        self.assertEqual(c2.color, "blue")

    def test_area(self):
        c1 = Circle(3, "red")
        c2 = Circle(5, "green")

        self.assertAlmostEqual(c1.compute_area(), math.pi * 3**2)
        self.assertAlmostEqual(c2.compute_area(), math.pi * 5**2)
```

The above set of tests is reasonble but we can do better by recognizing that both tests create the same Circle objects. If the initialization methods changes (maybe by adding a third required parameter) then changes must be made to both tests. The Python unittest module provides the `setUp()` and `tearDown()` methods for dealing with this.

```python
import unittest
from shapes import Circle
import math

class TestCircle(unittest.TestCase):

    def setUp(self):
        # do setup operations here for each test
        self.c1 = Circle(3, "red")
        self.c2 = Circle(5, "green")
        
    def test_colors(self):
        self.assertEqual(self.c1.color, "red")
        self.assertEqual(self.c2.color, "green")

        self.c1.change_color("blue")
        self.c2.change_color("blue")
        self.assertEqual(self.c1.color, "blue")
        self.assertEqual(self.c2.color, "blue")

    def test_area(self):
        self.assertAlmostEqual(self.c1.compute_area(), math.pi * 3**2)
        self.assertAlmostEqual(self.c2.compute_area(), math.pi * 5**2)

    def tearDown(self):
        # do teardown operations here for each test
        pass
```

Now run the tests:

```
$ python -m unittest test_shapes.py -v
test_area (test_shapes.TestCase1) ... ok
test_colors (test_shapes.TestCase1) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Let's add print statements to see the order that the various operations are ran:

```python
import unittest
from shapes import Circle
import math

class TestCircle(unittest.TestCase):

    def setUp(self):
        # do setup operations here for each test
        print("setUp")
        self.c1 = Circle(3, "red")
        self.c2 = Circle(5, "green")
      
    def test_colors(self):
        print("test_colors")
        self.assertEqual(self.c1.color, "red")
        self.assertEqual(self.c2.color, "green")

        self.c1.change_color("blue")
        self.c2.change_color("blue")
        self.assertEqual(self.c1.color, "blue")
        self.assertEqual(self.c2.color, "blue")

    def test_area(self):
        print("test_area")
        self.assertAlmostEqual(self.c1.compute_area(), math.pi * 3**2)
        self.assertAlmostEqual(self.c2.compute_area(), math.pi * 5**2)

    def tearDown(self):
        # do teardown operations here for each test
        print("tearDown")
```

Here is the output:

```
$ python -m unittest test_shapes.py
setUp
test_area
tearDown
.setUp
test_colors
tearDown
.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## setUpClass() and tearDownClass()

We saw above that `setUp()` and `tearDown()` run for each test. In some cases you will want to perform some operations once before all the tests and once after all the tests. For this the `setUpClass()` and `tearDownClass()` methods can be used:

```python
import unittest
from shapes import Circle
import math

class TestCircle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # do setup operations here for all tests once
        print("setUpClass")
    
    def setUp(self):
        # do setup operations here for each test
        self.c1 = Circle(3, "red")
        self.c2 = Circle(5, "green")
        
    def test_colors(self):
        self.assertEqual(self.c1.color, "red")
        self.assertEqual(self.c2.color, "green")

        self.c1.change_color("blue")
        self.c2.change_color("blue")
        self.assertEqual(self.c1.color, "blue")
        self.assertEqual(self.c2.color, "blue")

    def test_area(self):
        self.assertAlmostEqual(self.c1.compute_area(), math.pi * 3**2)
        self.assertAlmostEqual(self.c2.compute_area(), math.pi * 5**2)

    def tearDown(self):
        # do teardown operations here for each test
        pass
        
   @classmethod
    def tearDownClass(cls):
        # do teardown operations here for all tests once
        print("teardownClass")
```

By running the tests we see the order in which the various functions are executed:

```
$ python -m unittest test_shapes.py
setUpClass
setUp
test_area
tearDown

.setUp
test_colors
tearDown

.teardownClass

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

In the above nothing was done in `setUpClass()` or `tearDownClass()`. An example of using `setUpClass()` would be connecting to a database or generating a large file. For more details on the material above see the [video](https://www.youtube.com/watch?v=6tNS--WetLI) by Corey Schafer.

## Exercise 2

Add `setUp()`, `tearDown()`, `setUpClass()` and `tearDownClass()` to the tests of `circle_radius.py`. Or apply these methods to the tests of the scripts for your research work.

## Running multiple test files with TestSuite

Above we consider the source code `shapes.py` and the corresponding unit tests in `test_shapes.py`. What if your project is composed of multiple files such as `shapes.py` and `sizes.py`? How can you execute all the tests at once? The idea is to create a `TestSuite` and a `TestRunner` to run all the tests at once.

Here are the contents of `runner.py`:

```python
import unittest
import test_shapes
import test_sizes

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_shapes))
suite.addTests(loader.loadTestsFromModule(test_sizes))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
```

Run all the tests with:

```
$ python runner.py
setUpClass
test_area (test_shapes.TestCircle) ... setUp
test_area
tearDown

ok
test_colors (test_shapes.TestCircle) ... setUp
test_colors
tearDown

ok
teardownClass
test_thres (test_sizes.TestThresholds) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
