---
layout: homework
title: Homework 4 - Amaz(on)ing!
---

# Homework 4 - Amaz(on)ing!

## Introduction

In this homework you will practice

- numpy
- matplotlib
- pandas
- writing code in Jupyter Notebooks

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

You have just been hired as a data analyst for Amazon.  Your first assignment on the job is to analyze the review data for food products sold on Amazon.com.  To assist in your analysis, you have been given a [CSV file](reviews.csv) with information pertaining to more than 500,000 reviews from the site.

Each row in the CSV file contains the productID of the product being reviewed, the userID of the person making the review, the profile name of the reviewer, the helpfulnessNum and helpfulnessDen (which correspond the the numerator and denominator of the fraction of people who marked the review as helpful), the score given by the review, the time of the review, the title of the review, and the text of the review.


## Solution Description - IMPORTANT

For this assignment you must write your code in a Jupyter Notebook.  Because of the structure of the SciPy stack and the Jupyter Notebook, you do not need to write your code in separate functions.  Instead, use separate cells for each block of code you write.  You should turn in a neat, completed iPython Notebook File `amazon_analysis.ipynb` with your answers and explorations into the questions below clearly marked.

To get credit for this assignment, you must complete all of the tasks using a Pandas dataframe.  Because Pandas and numpy are vectorized, each task can be completed with at most a few lines of code.  You can (and should) complete this assignment without using a single for loop.


## Getting Started

Before the data can be analyzed, it must be imported.  Use the read_csv method from the Pandas module to read the data into a Pandas DataFrame.  The `pandas.read_csv()` method has many optional arguments that can be used to help it work for a wide variety of csv files.  When importing the reviews.csv file, set the encoding argument to "latin-1" and specify the data types of both of the helpfulness columns as np.float64.

Before moving on, be sure that the DataFrame was set up correctly.  The .head(n) method will display the first n rows of the DataFrame, default 5.

Once you are sure that the csv file was read in correctly, add a couple of columns to the DataFrame.  Notice that the "time" column consists of Unix timestamps.  Add a "datetime" column to the DataFrame - where the dates are represented as datetime objects - so that the dates are readable.  Also, add a "text_length" column which contains the number of characters in the text of the review.  These can be added in one line each using Pandas (and some functional programming for the character count).

Finally, use the drop_duplicates() method to ensure that any duplicate rows found in the existing csv file are not included in the DataFrame used for the analysis.


## Part 1 - Beginning Analysis

To get comfortable with Pandas and iPython Notebooks, complete the tasks below and display your results.  Remember to use a separate cell for each task you complete.

- Calculate the mean score of all the ratings in the dataset
- Calculate the median score of all the ratings in the dataset
- Plot the distribution of all the scores using a histogram
- Plot the distribution of the scores of reviews marked as a helpful by at least 7 people using a histogram
- Calculate the median length of the text of all the reviews
- Find the UserIDs of the users who wrote the ten longest reviews.  Display both the User IDs and length of each of review

## Part 2 - Grouping Data

In Pandas, the groupby command allows you to group the data together using certain columns, and perform calculations "groups" of rows.  Use the groupby command to help complete the tasks below:

- Find the number of (unique) products in the dataset
- Find the 5 products with the most reviews.  Display both the product IDs and the corresponding number of reviews

- Find the five users who wrote the most reviews.  Display the user IDs and the number of reviews
- Plot the distribution of the mean score of each user's reviews using a histogram

- Find the total number of reviews written each year.  Plot the results using a line graph.
- Calculate the mean score of the reviews written each year.  Plot the results using a line graph.

## Part 3 - Independent Analysis

Look back at the distribution of all of the scores in the dataset that you plotted in part 1.  Look closely at its shape.

Now, for three words of your choosing, plot the distribution of the scores of the reviews containing that word in the text.  Choose words that you think would alter the distribution you saw in part 1.  Try to choose words that you think will alter the distribution in different ways.  In addition to the plot, calculate and display the percentage of reviews that contain the word.

In a text cell underneath each of the 3 histograms, write a short explanation of why you chose the word, what you expected the resulting distribution to look like, and what the resulting distribution looks like in reality.  If the distribution looks differently than you expected, explain why you think that may be the case.  The quality of your written analysis will be considered in your grade!


##Grading

- Reading in CSV Data +5
- Adding appropriate columns +5 each (10 total)

- Part 1 Metrics and Plots: +5 each (30 total)
- Part 2 Metrics and Plots: +5 each (30 total)

- Part 3 Code: +10
- Part 3 Analysis: +15 (+0 if code does not produce histograms)




## Submission Instructions

Attach your `amazon_analysis.ipynb` file to your T-Square HW4 assignment submission.

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
