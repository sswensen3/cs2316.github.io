---
layout: homework
title: Homework 5
---

### Introduction
  
 -In this homework you will practice creating web applications.
 -
 + working with SQL and databases
 + processing CSV files
## Problem Description
  
You will be given a CSV file which has an inventory of items. The CSV file has the columns: itemName,value,quantity. You will be using this file to create a table called Inventory within an SQLite database with the primary key of the table being the itemName. You will also be creating an Owner class that will have the ability to sell and buy inventory by interacting with the database. The Owner class will keep track of owners' inventory and the amount of the cash they have. You will then create a main function that will allow a user to create multiple owners that can buy and sell inventory from the same Inventory table in a given database. Your table of inventory will have to update with each transaction that an owner completes. If updating the value of an item when buying or selling makes the value a non-integer, round that value to the nearest integer.

If an owner tries to sell something that's not in their inventory, or tries to buy something that they can't afford, or tries to buy something from the database that doesnt exist, please do not allow the code to throw errors. Use try and except statements and print a helpful message to the console that is relevant to whatever caused the error.  

The value of an item and the item name create a unique identifier for the inventory_dict.  If your inventory_dict has the Key/Value pair `("light", 15) : 2` and you buy a new light that has value `20`, your inventory dict should be updated to look like `{ ("light", 15) : 2 , ("light", 19) : 1 }`.


####Important Note: You need to use SQL queries on the db for most of the functions; points will not be given for manipulating csv data.

Here is a helpful link for understanding sqlite3 and creating local databases:
https://docs.python.org/3.5/library/sqlite3.html


## Solution Description
  
 ```Python
 
class Owner:
	"""The Owner class should have one class attribute db (initialized as None) which will represent a database connection object. Each owner instance should have instance variables that hold the owner's unique name, money, and a dictionary of their inventory in the form {item:(value, quantity)}
	"""

	def __init__(self, name, money = 500.0, inventory_dict = {}):
		"""money and inventory_dict have initital default values, but anything
		can be passed in to be the initial values.

		Parameters:
		self
		name: String
		money: float -- the Owner's money, is 500.0 if not given
		inventory_dict: dict -- keeps track of Owner's inventory, is {} if not given
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
		the Inventory table or there are no items left in the table, print a message to indicate this to the user.

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
		table with the value being the price for which it was sold. If the item is already in the Inventory table and has the same price as you're selling yours for, increase the count of that item. Otherwise, make sure to add a new row with your price, item_name, and count of 1. Then, decrease the count of that item (or remove it if the count is 1) from the inventory_dict. 

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
		same -- if the item is already in the table and has the same price as you're selling yours for, increase the count of that item. Otherwise, make sure to add a new row with that price. Update the owner's money accordingly.

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
		float -- the amount of money the user has plus the sum of the value of everything in inventory
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
 
def create_db(file_name):
	"""Creates a local SQLite database using the sqlite3 module and then creates a table called Inventory in the database. The table should be populated from a csv file. There will be three columns: itemName, Price, and Quantity. The primary key will be the itemName. Price and Quantity will both be stored as integers in the database.

	Parameters:
	file_name: String -- the name of the csv file that contains the inventory

	Return:
	a connection the the created database
	"""
	
def main(args):
	""" Create a main function that first calls create_db to create a local database containing a table called Inventory and populates it with the contents of a csv file. The CSV filename should be passed in as an 
	argument to the main function through the command line. Then the main function should allow the user to create as many owners as they want to. You need
	to keep track of those owners (in a dictionary), as the user should be allowed to select any owner at any point, and call the various 
	functions on them. 
	
	Your main method should have a prompt that asks the user which one of the owners they want to select, then
	from there, there should be a prompt asking which of the operations they want to call on the selected Owner. The user may not know 
	the item names in the Inventory table, and if this is the case, they should be able to prompt the main function to provide a list
	of all of the inventory names in the Inventory table. At any point the user should be able to go back to the previous prompt or
	quit out of the program.
	"""
 
 ```


Example shell interaction.

```
>>>What would you like to do next? create owner
>>>Great! What's your owner's name? Alex
>>>How much money does your owner have? 100.50
>>>How much inventory do they have? None
Owner created!
>>>What would you like to do next? buy inventory
>>>Which owner do you want to buy inventory for? Megi
>>>Great! Do you know the item name? Quit
Thanks for playing, Megi!
```
 
 
  
## Submission Instructions
  
 
 Attach your `hw5.py` file to your T-Square HW5 assignment submission.
 
 
## Verify Your T-Square Submission!
  
  Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.
