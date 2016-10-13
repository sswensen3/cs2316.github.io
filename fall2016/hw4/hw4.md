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

Write a Python module in `hw4.py` that includes the functions from the following tasks.

Task 1:

Your first task is to process the existing XML file and rewrite it in a cleaner, more tree-like form.  The XML file you were given is simply a root with 500 children.  That’s a pretty lame tree!  The XML tree you create should have a root containing the tag SP500.  The children of the root node will be nodes representing the sectors that make up the S&P 500.  Each sector is then broken down into several industries, so the children of the sector nodes will represent the industries that make up that sector.  Finally, the children of each industry node will represent the stocks that make up the industry.   

A sample section (for the Telecommunications Services sector) of the tree you are writing is below.  The tag names, attributes, and text of each element should be consistent with the example.   

```XML
<SP500>
    <Sector name="Telecommunications Services">
        <Industry name="Integrated Telecommunications Services">
            <Stock ticker="T">ATT Inc</Stock>
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
```

Use the following two functions to create the new XML file:

```Python
def readTree(filename):
	"""This function will read in the existing xml file and return a dictionary.
	The keys to the dictionary will be the sectors found in the xml file
	The value of each key will be another dictionary!
	This dictionary's keys will be the industries that make up that particular sector.
	The value of each key will be a list of the xml elements in the original tree for the stocks that make up that industry.
	
	Parameters: 
	filename: str - name of the existing xml file
	
	Return: dict which will be in the format above.	
	"""
```

```Python
def createTree(aDict):
	"""This function takes in the dictionary you created in readTree
	Iterate through the dictionary, and create an xml tree in the format described in the assignment
	Write that tree to a file called "output.xml"
	
	Parameters:
	aDict: dict - the dictionary you created in readTree
	
	Return: none
	"""
```
	
Task 2:

Now that you have experience working with XML files and you understand the hierarchical structure of the S&P 500, it’s time to move on to the even more exciting CSV pricing data! The first thing we need to do is get the CSV data in a usable format.  We will do that with the following functions:

```Python
def readCSV(filename):
	"""This function will read in the csv file, and return a list of lists. 
	Each list will be in the following format:[date, ticker, open, high, low, close, volume]. 
	The date should be in the form of a datetime object - (hint: look at datetime.datetime.strptime). 
	The ticker should be a string. The five numbers should be floats.
	
	Parameters:
	filename: str - csv file to be read
	
	Return: a nested list in the format specified above
	"""
```

```Python
def stock_dictionary(aList):
	"""This function will take in the list of lists created in readCSV and return a dictionary. 
	Each key will be a stock ticker. Each value will be a list of lists, with each list in the format 
	[dateObj, open, high, low, close, volume]. Each value should only contain information pertinent to the corresponding key.
	
	Parameters:
	aList: list - nested list that was created in readCSV
	
	Return: a dictionary with the information of the nested list
	"""
```

Perfect - we’re done processing the CSV data!  We have a dictionary with each stock’s ticker as a key, and information about that stock as a value.  Let’s write a few functions that use the dictionary to calculate some interesting metrics.

```Python	
def calcAvgOpen(aDict, ticker):
	"""This function takes in the dictionary you created in stock_dictionary and a ticker.  
	Return the average opening price for the stock as a float.
	
	Parameters:
	aDict: dict - created in the stock_dictionary function
	ticker: str - refers to a specific stock
	
	Return: float which is the average opening price of the stock
	"""
```

```Python
def findReturn(aDict, ticker, tup1, tup2):
	"""This function takes in the stock dictionary, a ticker, and two tuples.  The tuples
	represent dates, where each item in the tuple is an int.  
	It calculates the return of the stock between the two dates.  Calculate the return using
	the formula: (endPrice - startPrice)/startPrice. 
	Use the opening price on the starting date, and the closing price on the ending date. 
	Return this value as a float.
	In the event that there is no data for either of the two dates, print a message notifying user and
	return None.
	
	Parameters:
	aDict: dict - created in the stock_dictionary function
	ticker: str - refers to a specific stock
	tup1: tuple - represents the start date in the format (Month,Date,Year)
	tup2: tuple - represents the end date in the format (Month,Date,Year)
	
	Return: float of the mathematical return
	"""
```

```Python
def vwap(aDict, ticker):
	"""This function takes in the stock dictionary and a ticker.  Return the volume weighted average
	price (VWAP) of the stock.  In order to do this, first find the average price of the stock on
	each day.  Then, multiply that price with the volume on that day.  Take the sum of these values.  
	Finally, divide that value by the sum of all the volumes.  
	(hint: average price for each day = (high + low + close)/3)
	
	Parameters:
	aDict: dict - created in the stock_dictionary function
	ticker: str - refers to a specific stock
	
	Return: float which is the VWAP of the stock
	"""
```

```Python
def tickerFind(bDict, tup0):
	"""This function takes in the dictionary created in readTree and a tuple that contains a
	sector and an industry that belongs to that sector.  Return a list of tickers of the stocks that belong
	to that industry.
	
	Parameters:
	bDict: dict - created in the readTree function
	tup0: tuple - in the format (sector, industry)
	
	Return: list of tickers that belong to that industry
	"""
```

Awesome!  Now let's write a main function that puts it all together.  


Using the functions you have created:

1. Find the tickers associated with the sector and industry
2. Find the VWAP and average opening price associated with each ticker

		
To perform these calculations, your main function should call (in a logical order, with the appropriate parameters):

- readTree
- readCSV
- createTree (not used for the output of main but convenient to create the xml file for the user)
- stock_dictionary
- tickerFind
- vwap
- calcAvgOpen

Notes:

- If a CSV file name is not supplied:
Print out the ticker, vwap and average opening price on a single line

- If a CSV file name is supplied:
Write each ticker, vwap, and average opening price as a row in the CSV file

- If the ticker does not have pricing information, do not include the row in your print statements or CSV file		

```Python
def main(args):
	"""This function should have perform all of the tasks outlined above.
	
	Parameters:
	first: str - filename of given xml file ~ (SP_500.xml for us)
	second: str - filename of given csv file ~ (SP500_ind.csv for us)
	third: str - sector name
	fourth: str - industry name
	fifth: str - name of output csv file (OPTIONAL)
	
	Return: none
	"""
```

## Submission Instructions

Attach your `hw4.py` file to your T-Square HW4 assignment submission.

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
