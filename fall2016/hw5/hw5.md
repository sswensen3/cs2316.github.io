---
layout: homework
title: Homework 5
---

### Introduction
  
 -In this homework you will practice creating web applications.
 -
 - working with SQL and databases
 - processing CSV files
## Problem Description
  
 +You will be given a CSV file which has an inventory of items. The CSV file has the columns: itenName,value,quantity. You will be using this file to create a table with the primary key of the table being the itemName. You will also be creating an Owner class that will have the ability to sell and buy inventory. The Owner class will keep track of their inventory and the amount of the cash they have. You will then create a main function that will allow a user to create multiple owners that can buy and sell inventory from the same database. Your table of inventory will have to update with each transaction that an owner completes.

## Solution Description
 + 
 +```Python
 +
 +class Owner:
 +    """Onwers have a unique name, money, and a dictionary of their inventory in the form
 +    {item:(value, quantity)}
 +    """
 +
 +    def __init__(self, starting_cash = 500, inventoryDict = {}, database):
 +        """starting_cash and inventoryDict have initital default values, but anything
 +        can be passed in to be the initial values"""
 +
 +    def buyCheapest(self, item = None):
 +        """Buys the cheapest of the specified item, and if no item is specified,
 +        buys the cheapest thing in the database. The price to buy something is
 +        95% of its value.  Reduce the owners money by that much, decrease the count of that item in the database (or remove it if there's none left after you decreae the count), and add it to the owners inventoryDict, with the value
 +        being the price you paid for it. If you buy that item again, you will just increase the quantity of that item in your inventoryDict. If the owner does not have enough money to buy any of the items in the database print a message to the user that they do not have sufficient funds.
 +        """
 +
 +    def sellItem(self, item = None):
 +        """Sells the most expensive of the specified item (from the owner's inventory), and if no item is specified, sells the most expensive item in inventory.  The ammount of
 +         of money you make when you buy something is 105% its value. Increase
 +         the owners money by that much, add it to the database with the value
 +         being the price you sold it for (unless the item is already in the database, in which case, you just increase the count). Then, decrease the count of that item (or remove it if the count is 1) from the inventoryDict. 
 +         """
 +
 +    def fireSale(self):
 +        """Sells everything in inventory.  Because you are selling so much,
 +        you get 80%/ of the value of all items.  Remove everything from your
 +        inventoryDict and add it all to the database with value staying the same (if the item is already in the database just increase the count, and if not make sure to add a new row in for the item).
 +        Update the owners money accordingly.
 +        """
 +
 +    def ownerNetWorth(self):
 +        """Returns the total net worth of the owner, which is the ammount of
 +        money they have plus the sum of the value of everything in inventory.
 +        """
 +
 +    def buyAll(self, item = None):
 +        """Buys all available items of the specified item, if no item is given,
 +        defaults to the item with the lowest price for all of that item.  The
 +        price per item is 95%/ of the value.  update the database, inventoryDict,
 +        and the owners money.
 +        """
 +    def writeCSV(self):
 +    	"""
 +    	Creates a CSV file of the owner's inventoryDict. The columns of the CSV vile will be:
 +    	Item,Price,Quanity
 +    	If the owner has no inventory, then make sure to output a message rather than write a blank CSV file.
 +    	"""
 +
 +def createDatabase(file_name):
 +    """Creates a table from the csv file. The primary key will be the itemName. Price and Quantity will both be stores as integers in the database.
 +    """
 +
 +def main(args):
 +    """ Create a main function that first creates a table with the CSV file. The CSV file name should be passed in as an argument to the main function. Then the main should allow the user to create as many owners as they want to. You need to keep track of those owners, as the user should be allowed to select any owner at any point, and call the various functions on them. Your main should have a prompt that asks the user which one of the owners they want to select, then from there, they should have a prompt of which of the operations they want to call on the owners. The user may not know the item names in the database, and if this is the case, they should be able to prompt the main function to provide a list of all of the inventory names in the database. At any point the user should be able to go back to the previous prompt or quit out of the program.
 +    """
 +
 +```
 +
 +
  
## Submission Instructions
  
 +
 +Attach your `hw5.py` file to your T-Square HW5 assignment submission.
 +
 +
 ## Verify Your T-Square Submission!
  
  Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.
