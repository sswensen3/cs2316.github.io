---
layout: homework
title: Homework 1
---

# Homework 1

## Introduction

In this assignment you'll practice

- writing functions and modules,
- doing arithmetic calculations,
- simple text processing, and
- getting interactive input from the user.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.

## Problem Description

You're an eclectic programmer who often needs to convert between giraffe neck and football field lengths, calculate BMIs, calculate course grades, and extract area codes from phone numbers and other stuff.

## Solution Description

Write a module named `hw1` containing all the functions listed below. The specifications for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- whch you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

**`doctest`**

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v hw1.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

> Notice that some of the usage examples of functions that return floats are rounded (using the built-in [round function](https://docs.python.org/3/library/functions.html#round).
) and some are not. Why?

**IMPORTANT**: Do not modify the provided docstrings!

### Function: `gn_to_fbf`

```Python
    """Convert a length in giraffe necks to a length in football fields.

    Parameters:
    gns: float -- a length in giraffe necks

    Return: a float representing the equivalent length in football
    fields -- one giraffe neck is 80 inches, one football field is
    3600 inches.

    Usage examples:
    >>> gn_to_fbf(90)
    2.0
    """
```

### Function: `body_mass_index`

```Python
    """Return the body mass index for height (in inches) and weight (in pounds)

    Parameters:
    height: float -- height in inches
    weight: float -- weight in pounds

    Return: BMI: float -- given by BMI = (weight / height ** 2) * 703

    Usage examples:
    >>> round(body_mass_index(68, 145), 6)
    22.044766
    """
```

### Function: `cylinder_volume`

```Python
    """Calculate the volume of a cylinder given its radius and height.

    Paramters:
    radius: int or float -- the radius of the cylinder
    height: int or float -- the height of the cylinder

    Return: The volume of the cylinder, given by V = pi * radius**2 * height,
    where pi is the the value of math.pi

    Usage examples:
    >>> round(cylinder_volume(4, 5), 6)
    251.327412
    """
```

`pi` should be imported from the [math module](https://docs.python.org/3/library/math.html\#math.pi).

### Function: `widget_yield`

```Python
    """Calculate the number of widgets that can be built from the given
    number of gears, axles and springs.

    Parameters:
    gears: int -- the number of gears
    axles: int -- the number of axles
    springs: int -- the number of springs

    Return: an int representing the number of widgets can be made if
    one widget requires 4 gears, 2 axles and 5 springs.

    Usage examples:
    >>> widget_yield(12, 3, 15)
    1
    """
```

The number of widgets must be a whole number; you can't have half a widget. For example, if you have 12 gears, 3 axles, and 15 springs you can only make 1 widget even though there are enough gears and springs for 3 widgets.

Tip: You may find Python's built-in [min](https://docs.python.org/3/library/functions.html#min) function useful.


### Function: `area_code`

```Python
    """Extract are code from a 10-digit U.S. phone number formatted as
    ABC-DEF-GHIJ.

    Parameters:
    phone_number: str -- a 10-digit U.S. phone number formatted as ABC-DEF-GHIJ

    Return: str containing the first thee digits, 'ABC', from 'ABC-DEF-GHIJ'

    Usage Examples
    >>> area_code('123-456-7890')
    '123'
    """
```

Tip: The [find](https://docs.python.org/3/library/stdtypes.html#str.find) method and string slicing, or the [split](https://docs.python.org/3/library/stdtypes.html#str.split) method may be useful for this problem.

### Function: `course_avg`

```Python
    """Caclulate course average based on weighting in syllabus

    Keyword Parameters:
    exams: Sequence[int] -- 4 scores: 3 exams, last is the final exam
    hws: Sequence[int] -- homework scores

    Return: weighted average, where exam average is 60% of final
    grade, final exam is 20% of final grade, and homework average is
    20% of final grade.

    Usage examples:
    >>> course_avg([100, 90, 80, 70], [90, 80])
    85.0
    """
```

### Function: `course_grade`

```Python
    """Caclulate course average based on weighting in syllabus and return
    a str grade based on syllabus cutoffs

    Keyword Parameters:
    exams: Sequence[int] -- 4 scores: 3 exams, last is the final exam
    hws: Sequence[int] -- homework scores

    Return: 'A' if course_avg(exams, hws) >= 90
                else 'B' if course_avg(exams, hws) >= 80
                else 'C' if course_avg(exams, hws) >= 70
                else 'D' if course_avg(exams, hws) >= 60
                else 'F'

    Usage examples:
    >>> course_grade([100, 90, 80, 70], [90, 80])
    'B'
    """
```

### Function: `main`

Write a `main` function that takes a single argument named `args` (which you won't use) and call your `main` function from an `if __name__=="__main__"` block as discussed below. Your main function should prompt the user for their height and weight and print their BMI (using the function you wrote earlier) rounded to one decimal place.  An example program run might look like this:

```sh
$ python hw1.py
What is your height, in inches? 72
What is your weight, in pounds? 136
Your BMI is 18.4
```

#### Discussion of "main" functions in Python

Some programming languages have a `main` method or function that acts as the entry point for a program. When you run a Python program all the code in the source file is executed top to bottom. You can approximate a "main function" by putting code in an if-statement like this:

```Python
if __name__=="__main__":
    # code that executes only when this module is run as a script
```

You can make your code even cleaner by explicitly creating a main function and calling it from the `if __name__=="__main__"` block:

```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```

Following this pattern also allows you to run the `main` function explicitly when you import the module into the REPL, e.g.:

```Python
>>> import hw1
<module 'hw1' from '/Users/chris/cs2316/hw1/hw1.py'>
>>> hw1.main([])
What is your height, in inches? 72
What is your weight, in pounds? 136
Your BMI is 18.4
```

We recommend that you write all of your Python modules this way.

## Submission Instructions

Attach your `hw1.py` file to your T-Square HW1 assignment submission.

## Verify Your T-Square Submission!

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After uploading the files to T-Square you should receive an email from T-Square listing the names of the files that were uploaded and received. If you do not get the confirmation email almost immediately, something is wrong with your HW submission and/or your email. Even receiving the email does not guarantee that you turned in exactly what you intended.
- After submitting the files to T-Square, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the T-Square Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from T-Square to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files. Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute! (If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
