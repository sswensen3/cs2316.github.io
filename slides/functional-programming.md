% Functional Programming in Python
%% A brief introduction

# Functional Features in Python

Functions are first class, meaning they can be

- stored in variables and data structures
- passed as arguments to functions
- returned from functions

# Higher-Order Functions

A higher order function is a function that takes another function as a parameter or returns a function as a value. We've already used one:

```Python
>>> help(sorted)
...
sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
```

The second parameter, `key`, is a function. In general, a *sort key* is the part of an object on which comparisons are made in a sorting algorithm.

# Sorting without a `key`

Say we have a list of tuples, *(name, gpa, major)*:

```Python
>>> import pprint as pp
>>> studs = [("Stan", 2.5, "ISyE"), ("Kyle", 2.2, "CS"),
...          ("Cartman", 2.4, "CmpE"), ("Kenny", 4.0, "ME")]
```

The default sort order is simply elementwise by the default order for each type in the tuple:

```Python
>>> pp.pprint(sorted(studs))
[('Cartman', 2.4, 'CmpE'),
 ('Kenny', 4.0, 'ME'),
 ('Kyle', 2.2, 'CS'),
 ('Stan', 2.5, 'ISyE')]
```

Answer for yourself: what if two students had the same name?

# Sorting with a `key`

If we want a different sort order, we can define a function that extracts the part of each tuple by which we want to sort.

```Python
>>> def by_gpa(stud):
...     return stud[1]
...
>>> pp.pprint(sorted(studs, key=by_gpa))
[('Kyle', 2.2, 'CS'),
 ('Cartman', 2.4, 'CmpE'),
 ('Stan', 2.5, 'ISyE'),
 ('Kenny', 4.0, 'ME')]
```

`sorted` is a *higher-order function* because it takes a function as an argument.

# Lambda Functions

The `by_gpa` function is pretty simple. Instead of defining a named function, we can define it inline with an anonymous function, a.k.a., a *lambda function*:

```Python
>>> pp.pprint(sorted(studs, key=lambda t: t[1]))
[('Kyle', 2.2, 'CS'),
 ('Cartman', 2.4, 'CmpE'),
 ('Stan', 2.5, 'ISyE'),
 ('Kenny', 4.0, 'ME')]
```

The general form is `lambda <parameter_list>: <expression>`

The body of a lambda function is limited to a single expression, which is implicitly returned.

# `map`

Common task: build a sequence out of transformations of elements of an existing sequence. Here's the imperative approach:

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