# Docstrings

Modules, classes, and functions can have docstrings, which are strings that appear after the declaration (header) line and before the implementation code (or at the top of a module file). Here's a docstring for our hypotenuse function:

```Python
def hypotenuse(a, b):

    import math
    return math.sqrt(a*a + b*b)
```

# Doctest




```Python
python -m doctest -v doctest_example.py
```

See the [doctest documentation](https://docs.python.org/3/library/doctest.html) for more.
