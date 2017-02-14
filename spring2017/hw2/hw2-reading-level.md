---
layout: homework
title: Homework 2 - Reading Level
---

# Homework 2 - Reading Level

## Introduction

In this homework you will practice

- data structures,
- control structures,
- list comprehension, and
- using modules that you learn on your own from documentation.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TAs and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.

## Problem Description

You're a curious linguist with computer hacking skills and you want to use your Python skills to analyze text files! The functions below will help you figure out your writing level, the most occurring words in your text, and the number of complex words you're using!

## Solution Description

Write a Python module in `reading-level.py` that includes the following functions.

### `doctest`

The specifications for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:


```sh
python -m doctest -v reading-level.py
```

**IMPORTANT**: Do not modify the provided docstrings!


```Python
def normalize_text(text):
    """Return a list of all of the sentences in text with all whitespace
    (including newlines) collapsed to single spaces, punctuation
    removed and all characters converted to lowercase

    Parameters:
    text: str - text to normalize

    Return: a List[str] of sentences with single spaces between words, no
    punctuation, and all characters in lowercase

    Usage Examples:
    >>> normalize_text("I don't even have any skills. I have: Numchuk skills, bow hunting skills, computer hacking skills.")
    ['i dont even have any skills', 'i have numchuk skills bow hunting skills computer hacking skills']
    """
```

```Python
def word_counts(sentence_list):
    """Return a dictionary mapping words in normalized text to their
    counts in the text.

    Parameters:
    sentence_list: List[str] - a list of sentences

    Return: a Dict[str, int] whose keys are words and associated values are
    the number of times the word appears in the sentences in sentence_list

    Usage Examples: (Note technique for testing dict equality.)

    >>> word_counts(["i dont even have any skills", "i have numchuk skills \
    bow hunting skills computer hacking skills"]) == {'have': 2, 'numchuk': 1, \
    'hacking': 1, 'i': 2, 'even': 1, 'computer': 1, 'any': 1, 'bow': 1,\
    'hunting': 1, 'dont': 1, 'skills': 4}
    True
    """
```

```Python
def writing_level(sentence_list):
    """ Calculates the writing level of the text according to this formula:
    writingLevel = (0.39 x ASL) + (11.8 x AWL / 3) - 15.59
    ASL = average sentence length (number of words divided by the number of
    sentences not including white space characters)
    AWL = average word length (number of characters divided by number
    of words)

    Parameters:
    sentence_list: List[str] - list of all of the sentences

    Return: a float rounded to two decimal places representing the reading
    level of sentence_list

    Usage Examples:

    >>> writing_level(["i dont even have any skills", "i have numchuk skills bow hunting skills computer hacking skills"])
    6.46
    """
```

```Python
def filter_words(word_counts, length):
    """Return a list of tuples, List[Tuple[str, int]] - (word, count) containing
    words from word_counts that are greater than or equal to length.
     The list should be sorted in descending order with first the
    size of the word, and then the count of that word.

    Parameters:
    word_counts: Dict[str, int] whose keys are words and associated values
    are counts
    length: int - the minimum length of words to include in the List
    returned by this function

    Return: a List[Tuple[str, int]] sorted in descending order of
    word count, where the first element of each tuple is a word and the
    second element is the word's count. If there are no words equal to or
    greater than length, return an empty list.

    Usage Examples:
    >>> filter_words({'butcher': 1, 'baker': 2, 'candlestick': 1, 'the': 3, \
    'maker': 1}, 5)
    [('candlestick', 1), ('butcher', 1), ('baker', 2), ('maker', 1)]
    """
```

### `main`

Structure your main method as we have been taught:

```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```

The user will supply one command line argument to **your** Python script. The first argument to the `python` interpreter, `sys.argv[0]`, is the name of your script, i.e.,  `args[0] = "reading-level.py"`, so there will be 2 arguments in sys.argv, the second being the file name of the text.  A list of strings (sys.argv), should be passed as-is to the `main()` function to minimize confusion.

  * The first argument will be the file name of Python script (ie. `args[0] = "reading-level.py"`).
  * The second argument must be the name of a text file to read and analyze.
    + If the user supplies a file name on the command line and the file does not exist, you may allow the program to exit due to the missing file and let Python report that the file was not found.


Here's a snippet of code that checks for the existence of a file:

```Python
import os.path
os.path.exists("file_name.txt") # returns True if file_name.txt exists
```

Once you have a valid file name, read the file contents into a string. Here's a snippet of code that opens a file for reading as text and reads the file contents into a `str` variable:

```Python
infile = open(file_name, 'r') # opens file_name as readable file object infile
text = infile.read()          # dumps text data from infile into text variable
infile.close()                # closes infile
```

Once you read the contents of the file into a `str`, use the functions you created above to:

- normalize the text
- create a dictionary mapping words from the text to their counts,
- calculate the writing level of the text
- filter by 5, 6, and 7 letter words (using the filter_words function)
- print the following in a readable format:
    - reading level
    - total words
    - top 10 words at least 5 letters
    - top 10 words at least 6 letters
    - top 10 words at least 7 letters


Here's a sample program run, using the file [i-have-a-dream.txt](i-have-a-dream.txt) and then [twinkle.txt](twinkle.txt)


```sh
$ python reading-level.py i-have-a-dream.txt
Writing level: 9.83
total words: 1664
top words at least 5 characters long
('discrimination', 1)
('interposition', 1)
('demonstration', 1)
('tranquilizing', 1)
('nullification', 1)
('righteousness', 1)
('mountainside', 2)
('insufficient', 2)
('proclamation', 1)
('difficulties', 1)
top words at least 6 characters long
('discrimination', 1)
('interposition', 1)
('demonstration', 1)
('tranquilizing', 1)
('nullification', 1)
('righteousness', 1)
('mountainside', 2)
('insufficient', 2)
('proclamation', 1)
('difficulties', 1)
top words at least 7 characters long
('discrimination', 1)
('interposition', 1)
('demonstration', 1)
('tranquilizing', 1)
('nullification', 1)
('righteousness', 1)
('mountainside', 2)
('insufficient', 2)
('proclamation', 1)
('difficulties', 1)
```


```sh
$ python reading-level.py twinkle.txt
Writing level: 7.34
total words: 71
top words at least 5 characters long
('glorious', 1)
('twinkle', 4)
('diamond', 1)
('shining', 1)
('little', 2)
('wonder', 1)
('golden', 1)
('night', 2)
('light', 2)
('fills', 1)
top words at least 6 characters long
('glorious', 1)
('twinkle', 4)
('diamond', 1)
('shining', 1)
('little', 2)
('wonder', 1)
('golden', 1)
top words at least 7 characters long
('glorious', 1)
('twinkle', 4)
('diamond', 1)
('shining', 1)
```

## Grading

normalize text - 15 points
    punctuation removed - 5 points
    string converted to lower case - 5 points
    newline characters removed - 3 points
    each element in a list is a sentence - 2 points




word count - 15 points
    correct keys (words) - 5 points
    correct count of words for each key - 5 points
    returns a dictionary - 5 points



writing level - 20 points
    calculates the ASL correctly - 5 points
    calculates the AWL correctly - 5 points
    ignores whitespace characters - 2 points
    uses the correct formula to get the writing level - 5 points
    returns a float rounded to 2 decimal places - 3 points


filter words - 25 points
    correctly determines which words meet the length criteria - 5 points
    generates a tuple of the word and its count - 5 points 
    list of tuples sorted correctly - 10 points
        * by word length - 5 points
        * by count of the word - 5 points
    returns an empty list of no words meet the criteria - 3 points
    returns a list with the correct words - 2 points


main - 25 points
    correctly retrieves the file name specified in the command line - 5 points
    exits if incorrect file name is provided - 5 points
    opens the file correctly and reads it in as a string - 5 points
    makes correct calls to the previously defined functions - 5 points
    prints the outputs to the user in a readable format - 5 points 

## Submission Instructions

Attach your `reading-level.py` file to your T-Square HW2 assignment submission.

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
