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

You will be given a CSV file which has an inventory of items. The CSV file has the columns: item_name,value,quantity. You will be using this file to create a table called Inventory within an SQLite database with the composite key of the table being the item_name and value. You will also be creating an Owner class that will have the ability to sell and buy inventory by interacting with the database. The Owner class will keep track of owners' inventory and the amount of the cash they have. You will then create a main function that will allow a user to create multiple owners that can buy and sell inventory from the same Inventory table in a given database. Your table of inventory will have to update with each transaction that an owner completes. If updating the value of an item when buying or selling makes the value a non-integer, round that value to the nearest integer.

If an owner tries to sell something that's not in their inventory, or tries to buy something that they can't afford, or tries to buy something from the database that doesnt exist, please do not allow the code to throw errors. Use try and except statements and print a helpful message to the console that is relevant to whatever caused the error.  

The value of an item and the item name create a unique identifier for the inventory_dict.  If your inventory_dict has the Key/Value pair `("light", 15) : 2` and you buy a new light that has value `20`, your inventory dict should be updated to look like `{ ("light", 15) : 2 , ("light", 19) : 1 }`.


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
	owner's unique name, money, and a dictionary of their inventory in the form {item:(value, quantity)}
	"""
```

```Python
	def __init__(self, name, money = 500.0, inventory_dict = {}):
		"""money and inventory_dict have initital default values, but any other money amount can be 
		passed in to the init method

		Parameters:
		self
		name: String
		money: float -- the Owner's money, is 500.0 if not given
		inventory_dict: dict -- keeps track of Owner's inventory, is {} when first initialized}
		"""

	def buy_cheapest(self, item_name = None):
		"""Buys the cheapest item with the specified item_name, and if no item_name is specified,
		buys one of the cheapest items in the Inventory table. The price to buy something is
		95% of its value.  Reduce the Owner's money by that much, decrease the 
		count of that item in the Inventory table (or remove it if there are none left
		after you decrease the count), and add it to the Owner's inventory_dict, 
		with the value being the price they paid for it. If you buy that item again,
		you will just increment the quantity of that item in the inventory_dict. 
		If the owner does not have enough money to buy any of the items in 
		the Inventory table or there are no items left in the table, print a message to indicate 
		this to the user.

		Parameters:
		self
		item_name: String -- the name of the item to be bought

		Return:
		None
		"""

	def sell_item(self, item_name = None):
		"""Sells the most expensive of the specified item_name (from the owner's 
		inventory), and if no item_name is specified, sells the most expensive item
		in inventory.  The amount of of money you make when you buy something 
		is 105% of its value. Increase the owner's money by that much, and add it to the
		table with the value being the price for which it was sold. If the item is already 
		in the Inventory table and has the same price as you're selling yours for, increase 
		the count of that item. Otherwise, make sure to add a new row with your price, 
		item_name, and count of 1. Then, decrease the count of that item (or remove it if the 
		count is 1) from the inventory_dict. 

		Parameters:
		self
		item_name: String -- the name of the item to be bought

		Return:
		None
		"""

	def fire_sale(self):
		"""Sells everything in the Owner's inventory. Because you are selling so much,
		you earn only 80% of the value of each item you sell. Remove all items from your
		inventory_dict and add them all to the Inventory table with value staying the 
		same -- if the item is already in the table and has the same price as you're selling 
		yours for, increase the count of that item. Otherwise, make sure to add a new row with 
		that price. Update the owner's money accordingly.

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
		float -- the amount of money the user has plus the sum of the value of everything in 
		         inventory
		"""

	def buy_all(self, item_name = None):
		"""Buys as many of the specified item as possible. If no item_name is given,
		defaults to the item with the lowest price. The
		price per item is 95% of the value. Update the Inventory table, inventory_dict,
		and the owner's money accordingly (as stated in the methods above).

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
	columns: item_name, Price, and Quantity. The composite key of the table will be (item_name, value). 
	Price and Quantity will both be stored as integers in the database.

	Parameters:
	file_name: String -- the name of the csv file that contains the inventory

	Return:
	a connection the the created database
	"""
	
def main(args):
	""" Create a main function that first calls create_db to create a local database containing a 
	table called Inventory and populates it with the contents of a csv file. The CSV filename should be 
	passed in as an argument to the main function through the command line. Then the main function should 
	allow the user to create as many owners as they want to. You need to keep track of those owners (in a 
	dictionary), as the user should be allowed to select any owner at any point, and call the various 
	functions on them. 
	
	Your main method should have a prompt that asks the user which one of the owners they want to select, 
	then from there, there should be a prompt asking which of the operations they want to call on the 
	selected Owner. The user may not know the item names in the Inventory table, and if this is the case, 
	they should be able to prompt the main function to provide a list of all of the inventory names in the
	Inventory table. At any point, the user should be able to go back to the previous prompt or quit out of 
	the program.
	"""
 
```

Example shell interaction:

```
>>>What would you like to do next? create owner
>>>Great! What's your owner's name? Alex
>>>How much money does your owner have? 100.50
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

