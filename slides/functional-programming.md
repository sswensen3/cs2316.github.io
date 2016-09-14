% Functional Programming in Python
%% A brief introduction

# Functional Features in Python

Functions are first class, meaning they can be

- stored in variables and data structures
- passed as arguments to functions
- returned from functions

# Functions as Arguments

# `map`

# `filter`

# `reduce`

# List Comprehensions

# List Comprehensions

A list comprehension iterates over a (optionally filtered) sequence,
applies an operation to each element, and collects the results of these
operations in a new list.

```Python
>>> grades = [100, 90, 0, 80]
>>> [x for x in grades]
[100, 90, 0, 80]
>>> [x + 10 for x in grades]
[110, 100, 10, 90]
>>> [x + 50 for x in grades if x < 50]
[50]
```

List comprehensions are a concise way to accomplish transformations
which could otherwise be done with loops.


# Dictionary Comprehensions

# Generator Functions

# Generator Expressions

# Exercise

Write comprehension expressions that build the data structures from the [grades.py](../exercises/grades.py) exercise.