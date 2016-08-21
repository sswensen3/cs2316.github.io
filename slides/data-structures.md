% Data Structures

# Built-in Data Structures

Values can be collected in data structures:

- Lists
- Tuples
- Dictionaries
- Sets

This lecture just an overview. See the [Python documentation](https://docs.python.org/3.4/library/stdtypes.html) for
complete details.

# Lists

A list is an indexed sequence of Python objects.

- Create a list with square brackets

```Python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
```

- Create an empty list with empty square brackets or `list()` function

```Python
>>> empty = []
>>> leer = list()
```

- Normally you store elements of the same type in a list, but you
can mix element types

```Python
>>> mixed = [1, 'Two', 3.14]
>>> type(mixed[0])
<class 'int'>
>>> type(mixed[1])
<class 'str'>
>>> type(mixed[2])
<class 'float'>
```

# Creating Lists from Strings

- Create a list from a string with str's split() function:

```Python
>>> grades_line = "90, 85, 92, 100"
>>> grades_line.split()
['90,', '85,', '92,', '100']
```

- By default `split()` uses whitespace to delimit
elements. To use a different delimiter, pass as argument to
`split()`:

```Python
>>> grades_line.split(',')
['90', ' 85', ' 92', ' 100']
```

- The `list()` function converts any iterable object (like sequences)
to a list. Remember that strings are sequences of characters:

```Python
>>> list('abcdefghijklmnopqrstuvwxyz')
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z']
```

# Accessing List Elements

Individual list elements are accessed by index.

- First element at index 0

```Python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> boys[0]
'Stan'
```

- Negative indexes offset from the end of the list backwards

```Python
>>> boys[-1]
'Kenny'
```

- Lists are mutable, meaning you can add, delete, and modify
elements

```Python
>>> boys[2] = 'Eric'
>>> boys
['Stan', 'Kyle', 'Eric', 'Kenny']
```

# List Operators

The `in` operator tests for list membership. Can be negated with
not:

```Python
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> 'Kyle' in boys
True
>>> 'Kyle' not in boys
False
```

- The + operator concatenates two lists (note 'Butters' in list):

```Python
>>> boys + ['Butters']
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Butters']
The * operator repeats a list to produce a new list:
>>> ['Ni'] * 5
['Ni', 'Ni', 'Ni', 'Ni', 'Ni']
```

# Functions on Lists

Python provides several built-in functions that take list parameters.

- `len(s)` returns the number of elements in the list `s` (more
generally, the sequence `s`)

```Python
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> len(boys)
4
```

- `min(s)` returns the least element of `s`, `max(s)` returns the
greatest

```Python
>>> min(boys)
'Cartman'
>>> min([8, 6, 7, 5, 3, 0, 9])
0
>>> max(boys)
'Stan'
```

# The `del` Statement

The `del` statement deletes variables.

- Each element of a list is a variable whose name is formed by
indexing into the list with square brackets.

```Python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> boys[3]
'Kenny'
```

- Like any variable, a list element can be deleted with `del`

```Python
>>> del boys[3]
>>> boys
['Stan', 'Kyle', 'Cartman'] # You killed Kenny!
```

- A list variable is a variable, so you can delete the whole list

```Python
>>> del boys
>>> boys
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'boys' is not defined
```

# List Methods

Methods are invoked on an object (an instance of a class) by appending a dot, `.`, and the method name.

- `s.count(x)`: number of occurences of `x` in the sequence `s`

```Python
>>> surfin_bird = "Bird bird bird b-bird's the word".split()
>>> surfin_bird
['Bird', 'bird', 'bird', "b-bird's", 'the', 'word']
>>> surfin_bird.count('bird')
2
```

- `s.append(x)` adds the single element `x` to the end of `s`

```Python
>>> boys.append('Butters')
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Butters']
s.extend(t) adds the elements of t to the end of s
>>> boys.extend(['Tweak', 'Jimmy'])
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Butters', 'Tweak', 'Jimmy']
```

# List Methods

- `s.remove(x)` removes the first occurrence of `x` in `s`, or raises a
`ValueError` if `x` is not in `s`

```Python
>>> boys.remove('Kenny')
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Jimmy']
>>> boys.remove('Professor Chaos')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

- `s.pop()` removes and returns the last element of the list

```Python
>>> boys.pop()
'Jimmy'
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
```

# Slicing

Slicing lists works just like slicing strings (they're both sequences)

- Take the first two elements:

```Python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
>>> boys[0:2]
['Stan', 'Kyle']
```

- Take every second element, starting with the first:

```Python
>>> boys[::2]
['Stan', 'Cartman', 'Tweak']
>>> boys[0:5:2] # same as above
['Stan', 'Cartman', 'Tweak']
```

- Take the second from the end:

```Python
>>> boys[-2]
'Butters'
```

Note that slice operations return new lists.

# Aliases

Aliasing occurs when two or more variables reference the same object

- Assignment from a variable creates an alias

```Python
>>> brats = boys
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
```

Now boys and brats are aliases.

- Changes to one are reflected in the other, becuase they reference
the same object

```Python
>>> brats.append('Timmy')
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
```

# Copies

Operators create copies

```Python
>>> brats + ['Bebe', 'Wendy']
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy', 'Bebe',
'Wendy']
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
```

You have to reassign to the list to make an update:

```Python
>>> brats = brats + ['Bebe', 'Wendy'] # could also use shortcut +=
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy', 'Bebe',
'Wendy']
```

Notice that after the reassignment, `brats` is no longer an alias of
`boys`

```Python
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
```

# Slicing Creates Copies (Usually)

- Slice on the right hand side of an assignment creates a copy:

```Python
>>> first_two = boys[:2]
>>> first_two
['Stan', 'Kyle']
>>> first_two[0] = 'Stan the man'
>>> first_two
['Stan the man', 'Kyle']
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
```

- Slices on the left hand side allow for flexible assignment

```Python
>>> boys[0:2] = ['Randy', 'Sharon', 'Gerald', 'Sheila']
>>> boys
['Randy', 'Sharon', 'Gerald', 'Sheila', 'Cartman', 'Butters',
'Tweak', 'Timmy']
```

# A Few More List Operations

You can combine the elements of a list to form a string with `str`'s
`join()` method.

```Python
>>> aretha = ['R', 'E', 'S', 'P', 'E', 'C', 'T']
>>> "-".join(aretha)
'R-E-S-P-E-C-T'
```
`sorted()` function returns a new list

```Python
>>> sorted(aretha)
['C', 'E', 'E', 'P', 'R', 'S', 'T']
>>> aretha # Notice original is unchanged
['R', 'E', 'S', 'P', 'E', 'C', 'T']
```

`sort()` method modifies the list it is invoked on

```Python
>>> aretha.sort()
>>> aretha
['C', 'E', 'E', 'P', 'R', 'S', 'T']
```

# Example: Grades

Start with a list representing a line from a gradebook file

```Python
>>> grades_line = ['Chris', 100, 90, 95]
>>> grades_line
['Chris', 100, 90, 95]
```

Get the sublist containing just the grades by slicing

```Python
>>> grades = grades_line[1:]
>>> grades
[100, 90, 95]
```

Sum the grades using Python's built-in `sum()` function

```Python
>>> sum(grades)
285
```

- And get the average by dividing by the number of grades

```Python
>>> sum(grades) / len(grades)
95.0
```

# Tuples

Tuples are like lists, but are immutable.

```Python
Tuples are created by separating objects with commas
>>> pair = 1, 2
>>> pair
(1, 2)
```

Tuples can be used in assignments to "unpack" a sequence

```Python
>>> a, b = [1, 2]
>>> a
1
>>> b
2
```

Tuple assignment can be used to swap values

```Python
>>> b, a = a, b
>>> a, b
(2, 1)
```

# Dictionaries

A dictionary is a map from keys to values.

Create dictionaries with `{}`

```Python
>>> capitals = {}
```

Add key-value pairs with assignment operator

```Python
>>> capitals['Georgia'] = 'Atlanta'
>>> capitals['Alabama'] = 'Montgomery'
>>> capitals
{'Georgia': 'Altanta', 'Alabama': 'Montgomery'}
```

Keys are unique, so assignment to same key updates mapping

```Python
>>> capitals['Alabama'] = 'Birmingham'
>>> capitals
{'Georgia': 'Altanta', 'Alabama': 'Birmingham'}
```

# Dictionary Operations

Remove a key-value mapping with `del` statement

```Python
>>> del capitals['Alabama']
>>> capitals
{'Georgia': 'Atlanta'}
```

Use the `in` operator to test for existence of key (not value)

```Python
>>> 'Georgia' in capitals
True
>>> 'Atlanta' in capitals
False
```

Extend a dictionary with `update()` method, get values as a list
with values method

```Python
>>> capitals.update({'Tennessee': 'Nashville', 'Mississippi':
'Jackson'})
>>> capitals.values()
dict_values(['Jackson', 'Nashville', 'Atlanta'])
```

# Conversions to `dict`

Any sequence of two-element sequences can be converted to a `dict`

A list of two-element lists:

```Python
>>> dict([[1, 1], [2, 4], [3, 9], [4, 16]])
{1: 1, 2: 4, 3: 9, 4: 16}
```

A list of two-element tuples:


```Python
>>> dict([('Lassie', 'Collie'), ('Rin Tin Tin', 'German
Shepherd')])
{'Rin Tin Tin': 'German Shepherd', 'Lassie': 'Collie'}
```

Even a list of two-character strings:

```Python
>>> dict(['a1', 'a2', 'b3', 'b4'])
{'b': '4', 'a': '2'}
```

Notice that subsequent pairs overwrote previously set keys.

# Sets

Sets have no duplicates, like the keys of a `dict`. They can be iterated
over (we'll learn that later) but can't be accessed by index.

- Create an empty set with `set()` function, add elements with `add()` method

```Python
>>> names = set()
>>> names.add('Ally')
>>> names.add('Sally')
>>> names.add('Mally')
>>> names.add('Ally')
>>> names
{'Ally', 'Mally', 'Sally'}
```

- Converting to set a convenient way to remove duplicates

```Python
>>> set([1,2,3,4,3,2,1])
{1, 2, 3, 4}
```

# Set Operations

Intersection (elements in `a` *and* `b`)

```Python
>>> a = {1, 2}
>>> b = {2, 3}
>>> a & b # or a.intersetion(b)
{2}
```

Union (elements in `a` *or* `b`)

```Python
>>> a | b # or a.union(b)
{1, 2, 3}
```

# Set Operations

Difference (elements in `a` that are not in `b`)

```Python
>>> a - b # or a.difference(b)
{1}
```

Symmetric difference (elements in `a` or `b` but not both)

```Python
>>> a ^ b # or a.symmetric_difference(b)
{1, 3}
```

# Set Predicates

A predicate function asks a question with a `True` or `False` answer.

Subset of:

```Python
>>>a <= b # or a.issubset(b)
False
```

Proper subset of:

```Python
>>> a < b
False
```

# Set Predicates

Superset of:

```Python
>>> a >= b # or a.issuperset(b)
False
```

Proper superset of:

```Python
>>> a > b
False
```

# Closing Thoughts

Typical Python programs make extensive use of built-in data structures and often combine them (lists of lists, dictionaries of lists, etc)

- These are just the basics
- Explore these data structures on your own
- Read the books and Python documentation


This is a small taste of the expressive power and syntactic
convenience of Python's data structures.
