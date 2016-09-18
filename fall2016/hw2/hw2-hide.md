---
layout: homework
title: Homework 2
---

# Homework 2

## Introduction

In this homework you will practice

- control structures,
- functional programming, and
- using modules.

## Solution Description

Write a Python module in `hw2.py` that includes the following functions.

```Python
def letter_dict(text):
	"""Returns a dictionary with all the letters in a string, along with how many times they appear.

	Parameters:
	text: string -- a string with text

	Return: char_dict: dict -- dictionary with key as a character and value as the number of times it appears

	Usage examples:
	>>> letter_dict('Hello Everybody how aRe you doIng today?')
	{'?': 1, 'a': 2, 'g': 1, 'w': 1, 'y': 4, 'u': 1, 'b': 1, 'n': 1, 'o': 6, 'v': 1, 'd': 3, ' ': 6, 'e': 4, 't': 1, 'r': 2, 'l': 2, 'i': 1, 'h': 2}
	"""
```

```Python
def dict2tuples(char_dict, key=None):
	"""Convert a str:int dictionary to a list of (str, int) tuples, optionally sorted

	Parameters:
    char_dict: dict[str -> int]
    key: (optional) a key function to extract the element of the tuples by which to sort

	Return: a list[(str, int)], optionally sorted by key

    Usage example:
    >>> dict2tuples({'a': 2, 'b': 5, 'c': 1}, key=lambda t: t[1])
    [('c', 1), ('a', 2), ('b', 5)]
	"""
```

```Python
def draw_polygon(sides,t,wn):
	"""Returns the inner angle of a polygon and draw the polygon using turtle.

	Parameters:
	sides: int -- the number of sides of the polygon
	t: turtle - a turtle object created in main function
	wn: screen - the screen created in main function

	Return: angle: int -- The inner angle of a polygon given by (180*(sides-2))/sides

	Usage examples:
	>>> draw_polygon(5)
	108
	"""
```

```Python
def draw_bar_chart(bar_list):
	"""Converts a list of numbers between 0-300 into a bar chart with heights corresponding to the numbers
	then draws the bar chart using the turtle module.
	Bars in the range 0-100,100-200,200-300, should be red,blue and green respecitvely.
	It should write the height of each bar above the bar.

	Parameters:
	bar_list: Sequence(int) -- a list with numbers corresponding to the heights of each bar in a barchart
	t: turtle - a turtle object created in main function
	wn: screen - the screen created in main function


	Return: out_list: list -- number of red, green and blue bars in that order

	Usage examples:
	>>> draw_bar_chart([50,212,126,299,123,75])
	[2,2,2]
	"""
```

```Python
def draw_skyline(t,wn):
	"""Draws a skyline using turtle with at least ten buildings, with at least three different styles.

	Parameters:
	t: turtle - a turtle object created in main function
    wn: screen - the screen created in main function

    Return:
    None

    """
```

### `main`

Write a main function that does the following:

- ...

Of course, structure your main method as we have been taught:

```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```


## Submission Instructions

Attach your `hw2.py` file to your T-Square HW1 assignment submission.

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
