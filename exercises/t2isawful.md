---
layout: exercise
title: T^2 is Awful Exercise
---

# $T^2$ is Awful

## Introduction

In this assignment you will practice writing Python command-line utilities, file I/O, and dealing with poorly-formatted CSV files.

## Problem Description

You're a teacher who needs a list of student emails from your class.

## Solution Description

Write a program called `student_emails.py` that reads a CSV student roster downloaded form $T^2$ and prints to STDOUT a list of student names and emails of the form `Steve Lemme <slemme3@gatech.edu>`, one per line.

### Sample Output

```sh
$ python student_email.py t2isawful.csv
Jay Chandrasekhar <jchandrasekhar3@gatech.edu>
Kevin Heffernan <kheffernan3@gatech.edu>
Steve Lemme <slemme3@gatech.edu>
Paul Soter <psoter3@gatech.edu>
Erik Stolhanske <estolhanske3@gatech.edu>
```

## Tips and Considerations

You may find Python's [CSV module](https://docs.python.org/3/library/csv.html) helpful.