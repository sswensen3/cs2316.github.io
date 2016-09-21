---
layout: homework
title: Homework 2
---

# Homework 2

## Introduction

In this homework you will practice

- data structures,
- control structures,
- functional programming, and
- using modules.

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

## Problem Descrtiption

You're a curious linguist with computer hacking skills and you want to see, roughly, if [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law) holds for texts contained in files lying around on your disk.

## Solution Description

Write a Python module in `hw2.py` that includes the following functions.

```Python
def normalize_text(text):
    """Return copy of text in lowercase with punctuation removed.

    Parameters:
    text: str - text to normalize

    Return: str which is copy of text converted to lowercase with
    punctuation (the chars in string.punctuation) removed.

    Usage examples:
    >>> normalize_text("Numchuk skills, bow hunting skills, computer hacking skills...")
    'numchuk skills bow hunting skills computer hacking skills'
    """
```

```Python
def mk_word2count(text):
    """Return a dictionary mapping words in text to their count in text.

    Parameters:
    text: str -- string containing words separated by spaces

    Return: char_dict: dict -- dictionary whose keys are words and
    assocviated values are the number of times the word appears in text

    Usage examples:

    """
    word2count = {}
```

```Python
def dict2tuples(word_dict, key=None):
    """Convert a str:int dictionary to a list of (str, int) tuples, optionally sorted

    Parameters:
    word_dict: dict[str -> int]
    key: (optional) a key function to extract the element of the tuples by which to sort

    Return: a list[(str, int)], optionally sorted in descending order by key

    Usage example:
    >>> dict2tuples({'a': 2, 'b': 5, 'c': 1}, key=lambda t: t[1])
    [('b', 5), ('a', 2), ('c', 1)]
    """
    return sorted([(k, v) for k, v in word_dict.items()], key=key, reverse=True)
```

```Python
def normalize_counts(tuples, max_value=100):
    """Normalize the second values in tuples.

    Parameters:
    tuples: Sequence[(str, int)] -- (word, count) tuples
    max_value: int -- the max value of the normalized counts (min value is 0)

    Return: Sequence[(str, int)] with same first elements as tuples
    but whose second elements are normalized to the range 0 to
    max_value.

    Usage examples:
    >>> wctups = [('a', 200), ('the', 180), ('an', 160), ('shenannigans', 50)]
    >>> normalize_counts(wctups, 100)
    [('a', 100), ('the', 90), ('an', 80), ('shenannigans', 25)]
    """
```

```Python
def char_hist(bar_list):
    """Create a text-based bar chart from bar_list.

    Parameters:
    tuples: Sequence[(str, int)] -- (label, length) tuples

    Return: list[str] with one line per tuple in bar_list. Each line,
    a str in the returned list, has the right-aligned label, a |
    character, then length Xs

    Usage Examlpes:
    >>> from pprint import pprint
    >>> pprint(char_hist([('a', 10),('the', 9),('an', 8),('shenannigans', 2)]))
    ['           a | XXXXXXXXXX',
     '         the | XXXXXXXXX',
     '          an | XXXXXXXX',
     'shenannigans | XX']
    """
```

### `main`

More to come! Please check the T-Square announcements to see when this homework is updated.

Of course, structure your main method as we have been taught:

```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```


## Submission Instructions

Attach your `hw2.py` file to your T-Square HW2 assignment submission.

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
