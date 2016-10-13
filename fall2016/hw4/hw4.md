---
layout: homework
title: Homework 4
---

# Homework 4

## Introduction

In this homework you will practice

- processing CSV data
- processing XML data

## Problem Description

You have just been hired as an analyst for an investment firm.  Your first assignment is to analyze data for stocks in the S&P 500. The S&P 500 is a stock index that contains the 500 largest publicly traded companies.  Within the S&P 500, stocks are grouped together with similar stocks to form industries.  Similar industries are then combined together to form sectors.  Each stock belongs to a single industry, and each industry belongs to a single sector. 

You have been given two sources of data to work with.  The first is an XML file that contains the ticker, company name, sector, and industry for every stock in the S&P 500, as of Summer 2016.  

The second is a CSV file that contains pricing information for stocks in the S&P 500 between August 2009 and August 2010.  There is one row in the CSV file for every stock, on every date that the market was open. Each row contains the date as a string, the stock’s ticker, the day’s opening price, the day’s high price, the day’s low price, the day’s closing price, and the volume traded that day.

Note that stocks move in and out of the S&P 500.  Some stocks may be represented in the CSV file, but not in the XML file (and vice-versa).  However, most of the stocks that were in the S&P 500 in 2010 remain today. 

## Solution Description

Task 1:

Your first task is to process the existing XML file and rewrite it in a cleaner, more tree-like form.  The XML file you were given is simply a root with 500 children.  That’s a pretty lame tree!  The XML tree you create should have a root containing the tag SP500.  The children of the root node will be nodes representing the sectors that make up the S&P 500.  Each sector is then broken down into several industries, so the children of the sector nodes will represent the industries that make up that sector.  Finally, the children of each industry node will represent the stocks that make up the industry.   

A sample section (for the Telecommunications Services sector) of the tree you are writing is below.  The tag names, attributes, and text of each element should be consistent with the example.   

<SP500>
    <Sector name="Telecommunications Services">
        <Industry name="Integrated Telecommunications Services">
            <Stock ticker="T">AT&T Inc</Stock>
            <Stock ticker="CTL">CenturyLink Inc</Stock>
            <Stock ticker="FTR">Frontier Communications</Stock>
            <Stock ticker="VZ">Verizon Communications</Stock>
            <Stock ticker="WIN">Windstream Communications</Stock>
        </Industry>
        <Industry name="Wireless Telecommunications Services">
            <Stock ticker="CCI">Crown Castle International Corp.</Stock>
        </Industry>
    </Sector>
    .
    .
    .
</SP500>

Use the following two functions to create the new XML file:

def readTree(filename):
	"""This function will read in the existing xml file and return a dictionary.
	The keys to the dictionary will be the sectors found in the xml file
	The value of each key will be another dictionary!
	This dictionary's keys will be the industries that make up that particular sector.
	The value of each key will be a list of the xml elements in the original tree for the stocks that make up that industry.
	"""


def createTree(aDict):
	"""This function takes in the dictionary you created in readTree
	Iterate through the dictionary, and create an xml tree in the format described in the assignment
	Write that tree to a file called "output.xml"
	"""
    
Task 2:

Now that you have experience working with XML files and you understand the hierarchical structure of the S&P 500, it’s time to move on to the even more exciting CSV pricing data! The first thing we need to do is get the CSV data in a usable format.  We will do that with the following functions:
    
def readCSV(filename):
	"""This function will read in the csv file, and return a list of lists
	Each list will be in the following format: [date, ticker, open, high, low, close, volume]
	The date should be in the form of a datetime object - look at datetime.datetime.strptime
	The ticker should be a string
	The five numbers should be floats
	"""

def stock_dictionary(aList):
	"""This function will take in the list of lists created in readCSV and return a dictionary
	Each key will be a stock ticker
	Each value will be a list of lists, with each list in the format [dateObj, open, high, low, close, volume]
	Each value should only contain information pertinent to the corresponding key
	"""

Perfect - we’re done processing the CSV data!  We have a dictionary with each stock’s ticker as a key, and information about that stock as a value.  Let’s write a few functions that use the dictionary to calculate some interesting metrics.


## Submission Instructions

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
