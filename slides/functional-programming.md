% Functional Programming in Python
%% A brief introduction

# Functional Features in Python

Functions are first class, meaning they can be

- stored in variables and data structures
- passed as arguments to functions
- returned from functions

# Functions as Arguments

Remember the `key` argument to `sorted`?
```Python
>>> studs = [("Stan", 2.5, "ISyE"), ("Kyle", 2.2, "CS"),
...          ("Cartman", 2.4, "CmpE"), ("Kenny", 4.0, "ME")]
>>> def by_gpa(stud):
...     return stud[1]
...
>>> pp.pprint(sorted(studs, key=by_gpa))
[('Kyle', 2.2, 'CS'),
 ('Cartman', 2.4, 'CmpE'),
 ('Stan', 2.5, 'ISyE'),
 ('Kenny', 4.0, 'ME')]
```

`sorted` is a *higher-order function*. There are more general higher-order functions that are commonly used in functional programming.


# `map`

Common to build a sequence out of transformations of elements of an existing sequence. Here's the imperative approach:

```Python
>>> houses = ["Stark", "Lannister", "Targaryen"]
>>> shout = []
>>> for house in houses:
...     shout.append(house.upper())
...
>>> shout
['STARK', 'LANNISTER', 'TARGARYEN']
```

Heres' the functional approach:

```Python
>>> list(map(lambda house: house.upper(), houses))
['STARK', 'LANNISTER', 'TARGARYEN']
```
Note that `map` returns an iterator, so we pass it to the `list` constructor.

# `filter`

```Python
>>> nums = [0,1,2,3,4,5,6,7,8,9]
>>> filter(lambda x: x % 2 == 0, nums)
<filter object at 0x1013e87f0>
>>> list(filter(lambda x: x % 2 == 0, nums))
[0, 2, 4, 6, 8]
```

# List Comprehensions

A list comprehension iterates over a (optionally filtered) sequence,
applies an operation to each element, and collects the results of these
operations in a new list, just like `map`.

```Python
>>> grades = [100, 90, 0, 80]
>>> [x for x in grades]
[100, 90, 0, 80]
>>> [x + 10 for x in grades]
[110, 100, 10, 90]
```
We can also filter in a comprehension:

```Python
>>> [x + 50 for x in grades if x < 50]
[50]
```

Comprehensions are more Pythonic than using `map` and `filter` directly.

# Dictionary Comprehensions

First, zip:

```Python
words = ["Winter is coming", "Hear me roar", "Fire and blood"]
>>> list(zip(houses, words))
[('Stark', 'Winter is coming'), ('Lannister', 'Hear me roar'), ('Targaryen', 'Fire and blood')]
```

Dictionary comprehension using tuple unpacking:

```Python
>>> house2words = {house: words for house, words in zip(houses, words)}
>>> house2words
{'Lannister': 'Hear me roar', 'Stark': 'Winter is coming', 'Targaryen': 'Fire and blood'}
```

Of course, we could just use the `dict` constructor on the `zip` object.

```Python
>>> dict(zip(houses, words))
{'Lannister': 'Hear me roar', 'Stark': 'Winter is coming', 'Targaryen': 'Fire and blood'}
```


# `reduce`

```Python
>>> import functools
>>> functools.reduce(lambda x, y: x + y, [0,1,2,3,4,5,6,7,8,9])
45
```
Confirm this using the standard sum $\Sigma_{i=1}^{n} i = \frac{n(n + 1)}{2}$

Here's factorial:

```Python
>>> functools.reduce(lambda x, y: x * y, [1,2,3,4,5])
120
>>> functools.reduce(lambda x, y: x * y, range(1,6))
120
```

# Generator Functions

```Python
def class_dates(first, last, class_days):
    """Generate dates from first to last whose weekdays are in class_days

    >>> import datetime
    >>> begin = datetime.date(2016, 8, 22)
    >>> end = datetime.date(2016, 8, 25)
    >>> list(class_dates(begin, end, "TR"))
    [datetime.date(2016, 8, 23), datetime.date(2016, 8, 25)]
    """
    day = first
    # e.g., "MWF" => [0, 2, 4]
    class_day_ints = [i for i, letter in enumerate("MTWRFSU")
                           if letter in class_days]
    while day <= last:
        if day.weekday() in class_day_ints:
            yield day
        day += dt.timedelta(days=1)
```

# Generator Expressions

# Exercise

Write comprehension expressions that build the data structures from the [grades.py](../exercises/grades.py) exercise.