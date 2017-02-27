% SciPy - Data Analytics in Python

# The SciPy Stack

[SciPy](https://www.scipy.org/) is a Python-based ecosystem of libraries and tools for scientific computing and data analytics

- [iPython](http://ipython.org/)
- [Jupyter notebooks](http://jupyter.org/)
- [Numpy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Matplotlib](http://matplotlib.org/)

iPython is the primary way of interacting with the SciPy stack -- whether through the shell or a Jupyter notebook -- so we'll learn iPython first

# iPython

Two modes:

- Interactive shell

  - Replacement for `python` REPL

- Jupyter notebook

  - Interactive documents mixing text, executable code, graphics

# iPython Shell History

```sh
In [1]: ['Sage', 'Thyme', 'Oragano', 'Posh']
Out[1]: ['Sage', 'Thyme', 'Oragano', 'Posh']

In [2]: type(In[1])
Out[2]: str

In [3]: type(Out[1])
Out[3]: list

In [4]: spices = Out[1]

In [5]: spices
Out[5]: ['Sage', 'Thyme', 'Oragano', 'Posh']

In [6]: spices is Out[1]
Out[6]: True
```
`In` is a list, `Out` is a dict.

# iPython Help

Single `?` gives abbeviated version of python's `help`
```sh
In [7]: def add(a, b):
   ...:     """Return the result of + operation on a and b"""
   ...:     return a + b
   ...:

In [8]: add?
Signature: add(a, b)
Docstring: Return the result of + operation on a and b
File:      ~/cs2316/<ipython-input-7-af5293282e78>
Type:      function
```
Double `??` gives source code, if available.
```sh
In [9]: add??
Signature: add(a, b)
Source:
def add(a, b):
    """Return the result of + operation on a and b"""
    return a + b
File:      ~/cs2316/<ipython-input-7-af5293282e78>
Type:      function

In [10]:
```

# iPython Magic Commands

Special commands provided by iPython. A few examples:

- Run a Python script from within iPython:
```sh
In [35]: %run people.py
[<Stan, 2008-08-13, 150cm, 45kg>,
 <Kyle, 2008-02-25, 160cm, 50kg>,
 <Cartman, 2008-05-26, 140cm, 100kg>,
 <Kenny, 2009-07-30, 130cm, 40kg>]
```

- Paste multi-line formatt
```sh

```

Get a list of all magic commands with `%lsmagic`


# iPython Shell Commands

Run shell commands by prepending with a `!`

```sh
In [27]: !ls *.py
fun.py		grades.py	maths.py	people.py	pp.py

In [28]: pyscripts = !ls *.py

In [29]: pyscripts
Out[29]: ['fun.py', 'grades.py', 'maths.py', 'people.py', 'pp.py']
```

# iPython Automagic commands

With `automagic` turned on, some shell commands can be run as if they were built into iPython:

```sh
In [22]: pwd
Out[22]: '/Users/chris/cs2316'

In [23]: ls *.py
fun.py     grades.py  maths.py   people.py  pp.py
```

Toggle automagic on and off with `%automagic`.

These commands work with automagic: `%cd`, `%cat`, ` %cp`,` %env`, ` %ls`, ` %man`, ` %mkdir`, ` %more`, ` %mv`, ` %pwd`, ` %rm`,  and `%rmdir`


# Jupyter Notebooks

# NumPy

# Pandas

# Matplotlib
