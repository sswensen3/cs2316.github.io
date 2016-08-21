% Strings

# String Interpolation with `%`

The old-style (2.X) string format operator, %, takes a string with format specifiers on the left, and a single value or tuple of values on the right, and substitutes the values into the string according to the conversion rules in the format specifiers. For example:

```Python
>>> "%d %s %s %s %f" % (6, 'Easy', 'Pieces', 'of', 3.14)
'6 Easy Pieces of 3.140000'
```

Conversion rules on next slide ...


# Old-style (2.X) Conversion Rules

- `%s` string
- `%d` decimal integer
- `%x` hex integer
- `%o` octal integer
- `%f` decimal float
- `%e` exponential float
- `%g` decimal or exponential float
- `%%` a literal

# String Formatting with `%`

Specify field widths with a number between % and conversion rule:

```Python
>>> sunbowl2012 = [('Georgia Tech', 21), ('USC', 7)]
>>> for team in sunbowl2012:
...     print('%14s %2d' % team)
...
Georgia Tech 21
         USC  7
```

# Alignment with `%`

Fields right-aligned by default. Left-align with - in front of field width:

```Python
>>> for team in sunbowl2012:
...     print('%-14s %2d' % team)
...
Georgia Tech   21
USC             7
```

Specify n significant digits for floats with a .n after the field width:

```Python
>>> '%5.2f' % math.pi
' 3.14'
```

Notice that the field width indludes the decimal point and output is left-padded with spaces.

# String Interpolation with `format()`

New-style (3.X) interpolation uses the string method `format`:

```Python
>>> "{} {} {} {} {}".format(6, 'Easy', 'Pieces', 'of', 3.14)
'6 Easy Pieces of 3.14'
```

Old-style formats only resolve arguments by position. New-style formats can take values from any position by putting the position number in the `{}` (Notice that positions start with 0):

```Python
>>> "{4} {3} {2} {1} {0}".format(6, 'Easy', 'Pieces', 'of', 3.14)
'3.14 of Pieces Easy 6'
```

# Arguments to `format()`

Can also use named arguments, like functions:

```Python
>>> "{count} pieces of {kind} pie".format(kind='punkin', count=3)
'3 pieces of punkin pie'
```

Or dictionaries (note that there's one dict argument, number 0):

```Python
>>> "{0[count]} pieces of {0[kind]} pie".format({'kind':'punkin',
'count':3})
'3 pieces of punkin pie'
```

# String Formatting with `format()`

Conversion types appear after a colon:

```Python
>>> "{:d} {} {} {} {:f}".format(6, 'Easy', 'Pieces', 'of', 3.14)
'6 Easy Pieces of 3.140000'
```

Argument names can appear before the :, and field formatters appear between the : and the conversion specifier (note the < and > for left and right alignment):

```Python
>>> for team in sunbowl2012:
...     print('{:<14s} {:>2d}'.format(team[0], team[1]))
...
Georgia Tech  21
USC            7
```

# Sequence Unpacking

Recall that `sunbowl2012` is a list of tuples. You can unpack the tuple to supply its elements as individual arguments to format (or any function) by prepending tuple with * :

```Python
>>> for team in sunbowl2012:
...     print('{:<14s} {:>2d}'.format(*team))
...
Georgia Tech  21
USC            7
```

# Useful String Methods (1 of 4)

`str.find(substr)` returns the index of the first occurence of
`substr` in `str`

```Python
>>> 'foobar'.find('o')
1
```

`str.replace(old, new)` returns a copy of str with all occurrences of `old` replaced with `new`

```Python
>>> 'foobar'.replace('bar', 'fighter')
'foofighter'
```

`str.split(delimiter)` returns a list of substrings from `str`
delimited by `delimiter`

```Python
>>> 'foobar'.split('ob')
['fo', 'ar']
```

# Useful String Methods (2 of 4)

`str.join(iterable)` returns a string that is the concatenation of
all the elements of `iterable` with str in in between each element

```Python
>>> 'ob'.join(['fo', 'ar'])
'foobar'
```
`str.strip()` returns a copy of `str` with leading and trailing
whitespace removed

```Python
>>> ' landing   '.strip()
'landing'
```

`str.rstrip()` returns a copy of `str` with only trailing whitespace removed

```Python
>>> ' landing   '.rstrip()
' landing'
```

# Useful String Methods (3 of 4)

`str.rjust(width)` returns a copy of str that is `width` characters or `len(str)` in length, whichever is greater, padded with leading spaces as necessary

```Python
>>> 'rewards'.rjust(20)
'             rewards'
```

`str.upper()` returns a copy of `str` with each character converted to upper case.

```Python
>>> 'CamelCase'.upper()
'CAMELCASE'
```

`str.isupper()` returns `True` if `str` is all upper case

```Python
>>> 'CamelCase'.isupper()
False
>>> 'CAMELCASE'.isupper()
True
```

# Useful String Methods (4 of 4)

`str.isdigit()` returns `True` if `str` is all digits

```Python
>>> '42'.isdigit()
True
>>> '99 bottles of beer'.isdigit()
False
```

`str.startswith(substr_or_tuple)` returns `True` if `str` starts with `substr_or_tuple`

```Python
>>> 'a bang! a whimper'.startswith('a bang')
True
```

`str.endswith(substr_or_tuple)` returns `True` if `str` ends with `substr_or_tuple`

```Python
>>> 'bang! a whimper'.endswith('a whimper')
True
```