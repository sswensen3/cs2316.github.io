---
layout: homework
title: Homework 5
---

# Homework 5

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- You must include docstrings for all functions! There will be a point deduction if your code doesn't have docstrings. You should copy the docstrings from the instructions below, and feel free to add your own use cases for your own testing purposes.
- As stated at the bottom of this page, non-compiling code (code that does not run at all due to substantial runtime/syntax errors) will receive few to zero points! Make sure to test your submitted file and make sure the code runs.


### Introduction
  
In this homework you will practice:
 + working with SQL and databases
 + processing CSV files
 
 
## Problem Description
  
You are a developer creating a simple e-commerce marketplace app.

ou will be given a CSV file which has an inventory of items. The CSV file has the columns: itemName,value,quantity. You will be using this file to create a table with the primary key of the table being the itemName. You will also be creating an Owner class that will have the ability to sell and buy inventory. The Owner class will keep track of their inventory and the amount of the cash they have. You will then create a main function that will allow a user to create multiple owners that can buy and sell inventory from the same database. The owners table of inventory and money will have to update with each transaction that an owner completes.

If an owner trys to sell something not in their inventory, or trys to buy something that they cant afford, or trys to buy something from the database that doesnt exist, please do not allow the code to throw errors. Use try and expect statements and print a helpful message to the console that is relevant to whatever caused the error.

The owner's inventoryDict should be in the form {(item, price): count}


#### Important Note: You need to use SQL queries on the db for most of the functions; points will not be given for manipulating csv data.

Here is a helpful link for understanding sqlite3 and creating local databases:
https://docs.python.org/3.5/library/sqlite3.html


## Provided File
[items.csv](items.csv)

## Solution Description
  
#### Classes 

```Python
class Owner:
	"""The Owner class should have one class attribute db (initialized as None) which will represent a
	database connection object. Each owner instance should have instance variables that hold the 
	owner's unique name, money, and a dictionary of their inventory in the form {(item, price): count)}
	"""

	def __init__(self, name, database, starting_cash = 500):
		"""money has an initital default value, but any other money amount can be 
		passed in to the init method

		Parameters:
		self
		name: String
		money: int -- the Owner's money, is 500 if not given
		database: connection -- Use the Owner class variable 
		"""

	def buy_cheapest(self, item_name = None):
		"""Buys the cheapest of the specified item, and if no item is specified,
         	buys one of the cheapest items in the database. Reduce the owners money by the 
         	item's price, decrease the count of that item in the database (or remove
         	it if there's none left after you decrease the count), and add it to the
         	owners inventoryDict.  When adding to the inventoryDict, if the owner
         	has one of those items at the same price, increase the count.  If not, 
        	add it to the inventoryDict with a count of 1. If the owner does not have
         	enough money to buy what they passed in, or if they did not pass in anything,
         	if they do not have enough money to buy the cheapest thing in the database,
         	the database should print a message to the user that they do not have 
         	sufficient funds.
        	

		Parameters:
		self
		item_name: String -- the name of the item to be bought

		Return:
		None
		"""

	def sell_item(self, item_name = None):
		"""Sells the most expensive of the specified item (from the owner's 
		inventory), and if no item is specified, sells the most expensive item
		in inventory. Increase the owners money by the price and add the item, 
		price to the database and set the count to 1 (unless the item is already
		in the database, in which case, you just increase the count of the
		most expensive). Then, decrease the count of that item (or remove
		it if the count is 1) from the inventoryDict. 
         	


		Parameters:
		self
		item_name: String -- the name of the item to be bought

		Return:
		None
		"""

	def fire_sale(self):
		"""Sells everything in inventory.  Remove everything from your
		 inventoryDict and add it all to the database (if the item is 
		 already in the database just increase the count, and if not make 
		 sure to add a new row in for the item).
		 Update the owners money accordingly.
		 

		Parameters:
		self

		Return:
		None
		"""

	def net_worth(self):
		"""Returns the total net worth of the Owner, which is the amount of
		money they have plus the sum of the value of everything in their inventory.

		Parameters:
		self

		Return:
		int -- the amount of money the user has plus the sum of the value of everything in 
		         inventory
		"""

	def buy_all(self, item_name = None):
		"""Buys all available items of the specified item. If no item is given,
		 defaults to the item with the lowest cost for the sum of all the prices
		 of items with that name of that item. Update the database, inventoryDict,
		 and the owners money.
		 

		Parameters:
		self
		item_name: String -- name of the item to buy

		Return:
		None
		"""
```

#### Functions
 
``` Python
def create_db(file_name):
	"""Creates a local SQLite database using the sqlite3 module and then creates a table called 
	Inventory in the database. The table should be populated from a csv file. There will be three 
	columns: item_name, Price, and Quantity. The composite key of the table will be (item_name, price). 
	Price and Quantity will both be stored as integers in the database.

	Parameters:
	file_name: String -- the name of the csv file that contains the inventory

	Return:
	a connection to the created database
	"""
	
def main(args):
	""" Create a main function that first calls create_db to create a local database containing a 
	table called Inventory and populates it with the contents of a csv file. The CSV filename should be 
	passed in as an argument to the main function through the command line. Then the main function should 
	allow the user to create as many owners as they want to. You need to keep track of those owners (in a 
	dictionary), as the user should be allowed to select any owner at any point, and call the various 
	functions on them. 
	
	Your main method should have a prompt that asks the user which which of the operations they want to call
	then from there, there should be a prompt asking which of the one of the owners they want to select. The
	user may not know the item names in the Inventory table, and if this is the case, 
	they should be able to prompt the main function to provide a list of all of the inventory names in the
	Inventory table, with no duplicates. At any point, the user should be able to go quit out of 
	the program. Remember to close your database connection.
	"""
 
```

Example shell interaction:

```
>>>What would you like to do next? create owner
>>>Great! What's your owner's name? Alex
>>>How much money does your owner have? 100
Owner created!
>>>What would you like to do next? buy inventory
>>>Which owner do you want to buy inventory for? Megi
>>>Great! Do you know the item name? Quit
Thanks for playing, Megi!
```
 
 
  
## Submission Instructions
  
 
 Attach your `hw5.py` file to your T-Square HW5 assignment submission.
 
 **Homework 5 submissions should run without syntax or runtime errors! Non-compiling code will receive a 0. Be sure to follow the instructions below to verify that files are submitted correctly and the code works when you run it.**
 
 
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

-Non Compiling Code Will Recieve a 0

-Write your SQL statements as efficiently as possible. Try to do the majority of your data selection in the SQL statement and as little as possible in python. You may use multiple SQL statements as long as they do different things. For example, the following would be fine. use the SELECT statement buy_cheapest to get the cheapest item and its price, then in a separate statement UPDATE the count if it is greater than 1, or DELETE the row if count is 1.
