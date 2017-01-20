---
layout: homework
title: Homework 1 - Fit
---

# Homework 1 - `fit` Module

## Introduction

In this assignment you'll practice

- writing functions and modules,
- doing arithmetic calculations,
- simple text processing, and
- testing modules with doctest.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, T-Square login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

You run a phyical fitness contest modeled after Navy Special Warfare's physical screening test. You get data from contestants that includes times on a run, a swim, push-ups, pull-ups, and sit-ups and you must convert these times and numbers to a single score that can be used to rank fitness contest entries.

## Solution Description

You don't have the data file yet, but you want to be prepared so you wil create a module that caclulates elements of the composite score. Your module will be named `fit` and contain the functions listed below.

### `doctest`

The specifications for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

### Required Functions

```sh
python -m doctest -v fit.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

**IMPORTANT**: Do not modify the provided docstrings!

```Python
def time_seconds(time):
    """Take a time in MM:SS format and return the corresponding number of seconds

    Parameters:
    time: str -- time in MM:SS format

    Return:
    int -- number of seconds of a time specified in MM:SS format

    Usage Examples:
    >>> time_seconds("2:30")
    150
    """
```

```Python
def score(entry):
    """Take a dict containing the data for a participant and calculate a score

    Parameters:
    entry: dict[str -> Any] -- a dictonary containng the fitness test data for
           an entry in the contest

    Return:
    int -- score computed as follows:
           swim in seconds + run in seconds - pushups - situps - (pullups * 6)

    Usage Examples:
    >>> score({'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'})
    1055
    """
```

```Python
def average(data, event):
    """Take a list of dicts of fitness test entries and return the average for
    a single event

    Parameters:
    data: List[dict] -- a list of dictionaries of fitness test data
    event: str -- the name of an event, from the header of the data file

    Return:
    float -- the average score for that event. For run and swim, should be in
             seconds

    Usage Examples:
    >>> average([{'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'}, {'Run': '12:00', 'Push-ups': '100', 'Sit-ups': '100', 'Swim': '12:45', 'Name': 'Drogo', 'Pull-ups': '20'}], "Pull-ups")
    25.0
    """
    scores = []
```

```Python
def winner(data, event):
    """Take a list of dicts of fitness test entries and return the winner of
    event

    Parameters:
    data: List[dict] -- a list of dictionaries of fitness test data
    event: str -- the name of an event, from the header of the data file

    Return:
    (str, int) -- a tuple with the name of the winner of the event and the score
                  they got for that event. Swim and run should be in seconds

    Usage Examples:
    >>> winner([{'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'}, {'Run': '12:00', 'Push-ups': '100', 'Sit-ups': '100', 'Swim': '12:45', 'Name': 'Drogo', 'Pull-ups': '20'}], "Pull-ups")
    ('Tyrion', 30)
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `fit` module in the Python REPL to test your functions as you write and modify them. For example, ssuming you're in the same directory as your `fit.py` file:

```Python
Python 3.5.2 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import fit
>>> fit.time_seconds("2:30")
150
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(fit)
```

## Grading

- 50 points for having all required functions that can be called with the right parameters but not necessarily returning correct values
- 10 points for each correctly implemented function named exactly as listed above with docstrings as provided (40 points total)
- 10 points for following instructions, e.g., including your name, T-Square and GTID, indenting with four spaces, correctly naming your module and file

## Turn-in Procedure

Submit your `fit.py` file on T-Square as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

## Verify the Success of Your Submission to T-Square

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After uploading the files to T-Square you should receive an email from T-Square listing the names of the files that were uploaded and received. If you do not get the confirmation email almost immediately, something is wrong with your HW submission and/or your email. Even receiving the email does not guarantee that you turned in exactly what you intended.
- After submitting the files to T-Square, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the T-Square Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from T-Square to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files.\footnote{Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute!}
(If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
