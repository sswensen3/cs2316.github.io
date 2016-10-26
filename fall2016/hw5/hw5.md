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
  
You will be given a CSV file which has an inventory of items. The CSV file has the columns: itenName,value,quantity. You will be using this file to create a table with the primary key of the table being the itemName. You will also be creating an Owner class that will have the ability to sell and buy inventory. The Owner class will keep track of their inventory and the amount of the cash they have. You will then create a main function that will allow a user to create multiple owners that can buy and sell inventory from the same table ina  given database. Your table of inventory will have to update with each transaction that an owner completes.  If updateing the value of an 
item when buying or selling makes the value a non integer, round that value to the nearest integer.

If an owner trys to sell something not in their inventory, or trys to buy something that they cant afford, or trys to buy something
from the database that doesnt exist, please do not allow the code to throw errors.  Use try and expect statements and print a helpful
message to the console that is relevant to whatever caused the error.  

The value of an item and the item name create a unique identifier for the inventoryDict.  If your inventoryDict has the Key/Value pair {(light, 15):2 } and you buy a new light that has value 20, your inventory dicty should be updated to look like { (light, 15):2 , (light, 19):1}.


####Important Note: You need to use SQL queries on the db for most of the functions, points will not be given for manipulating csv data.

Here is a helpful link for understanding sqlite3 and creating local databases:
https://docs.python.org/3.5/library/sqlite3.html


## Solution Description
  
 ```Python
 
class Owner:
	"""Each owner instance should have instance variables that hold the owner's unique name, money, and a dictionary of their inventory in the form   {item:(value, quantity)}
	"""

	def __init__(self, name,  db, startingCash = 500.0, inventoryDict = {}):
		"""starting_cash and inventoryDict have initital default values, but anything
		can be passed in to be the initial values

		Parameters:
		self
		name: String
		db: the database connection
		startingCash: float -- is 500.0 if not given
		inventoryDict: dict -- is {} if not given

		"""

	def buyCheapest(self, item = None):
		"""Buys the cheapest of the specified item, and if no item is specified,
		buys one of the cheapest items in the table. The price to buy something is
		95% of its value.  Reduce the owners money by that much, decrease the 
		count of that item in the table (or remove it if there's none left
		after you decreae the count), and add it to the owners inventoryDict, 
		with the value being the price you paid for it. If you buy that item again,
		you will just increase the quantity of that item in your inventoryDict. 
		If the owner does not have enough money to buy any of the items in 
		the table or there are no items left in the table, print a message to indicate this to the user.


		Parameters:
		self
		item: String -- the name of the item to be bought


		Return:
		None
		"""

	def sellItem(self, item = None):
		"""Sells the most expensive of the specified item (from the owner's 
		inventory), and if no item is specified, sells the most expensive item
		in inventory.  The ammount of of money you make when you buy something 
		is 105% its value. Increase the owners money by that much, add it to the
		table with the value being the price you sold it for. If the item is already in the table and has the same price as you're selling yours for, increase the count of that item. Otherwise, make sure to add a new row with your price, item name, and count of 1. Then, decrease the count of that item (or remove it if the count is 1)
		from the inventoryDict. 


		Parameters:
		self
		item: String -- the name of the item to be bought


		Return:
		None
		"""

	def fireSale(self):
		"""Sells everything in inventory. Because you are selling so much,
		you get 80% of the value of all items. Remove everything from your
		inventoryDict and add it all to the table with value staying the 
		same -- if the item is already in the table and has the same price as you're selling yours for, increase the count of that item. Otherwise, make sure to add a new row with that price. Update the owners money accordingly.


		Parameters:
		self

		Return:
		None
		"""



	def ownerNetWorth(self):
		"""Returns the total net worth of the owner, which is the ammount of
		money they have plus the sum of the value of everything in inventory.


		Parameters:
		self


		Return:

		totalNewWorth: float -- the amount of money the user has plus the sum of the value of everything in inventory
		"""

	def buyAll(self, item = None):
		"""Buys as many available items of the specified item as possible, if no item is given,
		defaults to the item with the lowest price for all of that item.  The
		price per item is 95%/ of the value.  update the table, inventoryDict,
		and the owners money accoridngly (as stated in the methods above).


		Parameters:
		self
		item: String -- name of the item to buy


		Return:
		None
		"""
 
def createDatabase(file_name):
	"""Creates a local mysql database using sqlite3 module and then creates a table from the csv file that contains the contents in that file. The primary key will be the itemName. 
	Price and Quantity will both be stored as integers in the database.

	Parameters:
	file_name: String -- the name of the csv file that contains the inventory

	Return:
	db: a connection the the created database

	"""


 
def main(args):
	""" Create a main function that first creates a local database and then creates a table and populates it with the contents of the CSV file. The CSV file name should be passed in as an 
	argument to the main function. Then the main should allow the user to create as many owners as they want to. You need
	to keep track of those owners, as the user should be allowed to select any owner at any point, and call the various 
	functions on them. Your main should have a prompt that asks the user which one of the owners they want to select, then
	from there, they should have a prompt of which of the operations they want to call on the owners. The user may not know 
	the item names in the inventory table, and if this is the case, they should be able to prompt the main function to provide a list
	of all of the inventory names in the inventory table. At any point the user should be able to go back to the previous prompt or
	quit out of the program.
	"""
 
 ```


Example shell interaction.

```
>>>Welcome to Cat Sim v1.0. What is your name? Megi
Hello Megi
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
