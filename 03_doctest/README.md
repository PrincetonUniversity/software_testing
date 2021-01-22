# doctest

There is a fundamentally different approach to testing using the [`doctest`](https://docs.python.org/3/library/doctest.html) module. This
involves writing tests inside the docstrings and then executing these tests. The advantage of this approach is it combines writing
documentaion with testing. Both of these tend to get neglected. For researchers who are trying to write some tests and some documentation
this may be the best approach for you.

#### Example 1

```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Run the code:

```
$ software_testing/03_doctest
$ python example.py
```

If there is no output then all the tests passed. To see the explicit report:

```
$ python example.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
Trying:
    factorial(30)
Expecting:
    265252859812191058636308480000000
ok
Trying:
    factorial(-1)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
ok
Trying:
    factorial(30.1)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
ok
Trying:
    factorial(30.0)
Expecting:
    265252859812191058636308480000000
ok
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
2 items passed all tests:
   1 tests in __main__
   6 tests in __main__.factorial
7 tests in 2 items.
7 passed and 0 failed.
Test passed.
```

It is not necessary to include the `if __name__ == "__main__"` block. That is, one can also run the tests under doctest with this command:

```
$ python -m doctest example.py -v
```

#### Example 2

Here's another example where a list of two-tuples is sorted according to a custom criteria:

```python
def custom_sort(x):
  """Return sorted list of two-tuples by first item plus square of second item.

  >>> custom_sort([(3, 2), (5, 1), (1, 2)])
  [(1, 2), (5, 1), (3, 2)]

  >>> custom_sort([(1, 2), (0, 1), (3, 2)])
  [(0, 1), (1, 2), (3, 2)]

  >>> custom_sort([])
  []
  
  >>> custom_sort(42)
  Traceback (most recent call last):
      ...
  TypeError: 'int' object is not iterable
  """

  return sorted(x, key=lambda u: u[0] + u[1]**2)
```

```
$ python -m doctest example2.py -v
Trying:
    custom_sort([(3, 2), (5, 1), (1, 2)])
Expecting:
    [(1, 2), (5, 1), (3, 2)]
ok
Trying:
    custom_sort([(1, 2), (0, 1), (3, 2)])
Expecting:
    [(0, 1), (1, 2), (3, 2)]
ok
Trying:
    custom_sort([])
Expecting:
    []
ok
Trying:
    custom_sort(42)
Expecting:
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
ok
1 items had no tests:
    best
1 items passed all tests:
   4 tests in best.custom_sort
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
```

#### About testing for exceptions

doctest will not try to compare the exact traceback of the exception with the test version. This is because the traceback often contains custom file paths. Instead it looks for the `Traceback` header and the type of exception. You could also use the full exception in the test.

### More features of doctest

+ You can put the tests in a text file: `$ python -m doctest -v mytests.txt`
+ Imported modules are not searched for tests
+ ''In most cases a copy-and-paste of an interactive console session works fine, but doctest isn’t trying to do an exact emulation of any specific Python shell.''

### Python 3 Module of the Week

Check out the examples here: [https://pymotw.com/3/doctest/](https://pymotw.com/3/doctest/)

### Exercise

Try writing tests using [`doctest`](https://docs.python.org/3/library/doctest.html) for the code below for for a piece of code you use for your research:

```python
import math

def circle_area(radius):
    return math.pi * radius**2
```
