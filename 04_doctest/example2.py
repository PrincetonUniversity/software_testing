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
