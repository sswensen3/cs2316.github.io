---
layout: homework
title: Homework 3 - Pet Store
---

# Homework 3 - Pet Store

## Introduction

In this homework you will practice

- csv reading
- class dunder functions
- using instance variables
- class specific funtions
- writing a main function

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

You have decided to open a Pet Store!  However you quickly realize that in order to have a well run pet store you are going to need some sort of inventory system to keep track of all the pets you have for sale and how much money the pet store has. You will create a Pet class that defines the properties of a Pet, then create a Pet Store class that will manage an inventory of Pet objects.  You will also need to be able to populate the Pet Store based on a csv file with information on pets.  

## Solution Description

In this homework you will be writing 2 classes, a method to read in data from a csv file, and a main method to call all of the methods that you write. 

## Doctest

The specifications for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:


```sh
python -m doctest -v reading-level.py
```

**IMPORTANT**: Do not modify the provided docstrings!

## Code

Create a python file with the following classes

### `Pet`

```Python
class Pet:
    """An object of Pet will have a species, name, age, color, and price.  The
    Pet object should also be able to be printed in an informative manner.
    """
    
    def __init__(self, species, name, age, color, price):
        """Creates a new pet object with the instance attributes of its species,
         name, age, color, and price.

         Parameters:
            self
            species: String
            name: String
            age: Int -- in years
            color: String -- color of the Pet
            price: Int -- price in dollars for someone to buy the pet from your
                store
        """

    def __repr__(self):
        """Create a string representation for each pet created.  This will
        mostly be used when printing out the objects in main, so you may
        write this in any way that conveys all relevant information about the
        Pet

        Parameters:
            self
        """

    def __eq__(self, other):
        """Compares two Pets to test equality.  Pets are equal if their species,
        name, and age are the same.  When checking names, species, and age,
        the code should be case insensitive, so "bill" and "Bill" are the same
        name

        Parameters:
            self
            other: Pet Object -- the second Pet you are comparing to the first

        Usage Examples:
        >>> a = Pet("Dog", "Alex", 6, "Gold", 150)
        >>> b = Pet("Dog", "alex", 6, "gold", 400)
        >>> a == b
        True
        """

    def __gt__(self, other):
        """Comparison function to allow sorting of Pets.  The order for Pets
        is by age, oldest to youngest.  If two Pets have the same age, sort by
        name alphabetically.

        Parameters:
            self
            other: Pet Object -- the second Pet you are comparing to the first

        Usage Examples:
        >>> a = Pet("Dog", "Alex", 8, "Gold", 150)
        >>> b = Pet("Dog", "Todd", 6, "gold", 400)
        >>> a > b
        True

        >>> a = Pet("Dog", "Alex", 6, "Gold", 150)
        >>> b = Pet("Dog", "Todd", 6, "gold", 400)
        >>> a > b
        True
        """
```
### `Pet Store`
```Python
class PetStore:
    """Here you will write the inventory management system for your Pet Store.
    The Pet Store will let you as the owner sell your cheapest pet of a specific
    species, sell all of a specific species, cut the price of a specific species
    in half, or breed two Pets of the same, specified, species.
    """

    def __init__(self):
        """ Initializes a Pet Store object with two instance variables: money
        and inventory.  When the Pet Store first opens, you should start with
        $1000 and a dictionary with the keys "Cat", "Bird", "Dog", and "Snake"
        with the values of each key being an empty list.  This dictionary will
        hold the Pet Store's inventory. As you add Pet's to the Pet Store,
        they will be added to the list that is the value of the key
        corresponding to the Pet's species.  FYI, the test cases will not work
        correctly until this method is complete.  For the test cases to work you
        must name the instance variables money and inventory.

        IF YOU USE DIFFERENT KEYS IN YOUR INVENTORY YOU MAY LOSE POINTS

        Parameters:
            self
        """

    def add_pet(self, pet):
        """Adds a pet to the pet store.  Be sure to add the pet to the correct
        part of the inventory dictionary.

        Parameters:
            self
            pet: Pet Object -- pet to add to your pet store

        Usage Examples:
            >>> ps = PetStore()
            >>> cat = Pet("Cat", "Meowth", 17, "White", 400)
            >>> ps.add_pet(cat)
            >>> ps.inventory["Cat"][0] == cat
            True
        """


    def sell_cheapest(self, species):
        """Sells the cheapest pet of the specified species, increasing the
        Pet Store's money by the price of the pet and removing the pet you just
        sold from the inventory. If there are two pets that are the same price
        and that price is the cheapest of those species, sell the one who's name
        comes first alphabetically.
        If there are no Pets of the specified species in inventory, please
        print a message to the user to let them know.
        Hint: This is not the same sorting as Pet's comparator function

        Parameters:
            self
            species: String -- the species you want to sell

        Usage Examples:
            >>> ps = PetStore()
            >>> cat = Pet("Cat", "Meowth", 17, "White", 400)
            >>> cat2 = Pet("Cat", "James", 10, "Blue", 100)
            >>> ps.add_pet(cat)
            >>> ps.add_pet(cat2)
            >>> ps.sell_cheapest("Cat")
            >>> ps.inventory["Cat"][0] == cat
            True
        """

    def sell_all(self, species):
        """Sells all pets of the specified species. The PetStore's money should
        increase by the price of all the Pets sold.  The PetStore's inventory
        should reflect you no longer own any of that species.
        If there are no Pets of the specified species in inventory, please
        print a message to the user to let them know.

        Parameters:
            self
            species: String -- the species you want to sell

        Usage Examples:
            >>> ps = PetStore()
            >>> cat = Pet("Cat", "Meowth", 17, "White", 400)
            >>> cat2 = Pet("Cat", "James", 10, "Blue", 100)
            >>> ps.add_pet(cat)
            >>> ps.add_pet(cat2)
            >>> ps.sell_all("Cat")
            >>> ps.money == 1500
            True
        """



    def discount(self, species):
        """Cuts the price of all of the specified animals in half.  If the
        resulting price is a float, floor the result so that it is an integer
        If there are no Pets of the specified species in inventory, please
        print a message to the user to let them know.

        Parameters:
            self
            species: String -- the species you want to discount

        Usage Examples:
            >>> ps = PetStore()
            >>> cat = Pet("Cat", "Meowth", 17, "White", 400)
            >>> ps.add_pet(cat)
            >>> ps.discount("Cat")
            >>> ps.inventory["Cat"][0].price == 200
            True
        """

    def breed(self, species, name):
        """Breeds the two oldest animals of the given species.  If there are
        more than two animals that qualify as oldest, sort next by name
        Alphabetically (if you have the following Dogs and their ages: (Bill,7),
        (Marie,8), and (Max, 7), then Marie and Bill would breed, since Bill
        comes before Max alphabetically).  Set the age of the baby as 1, price
        as 500, and the name as specified in the parameter.  The color of the
        baby is the same as the oldest parent, and if both have the same age,
        the color of the parent with the first name alphabetically. Remember to
        add the new baby pet to your inventory.
        If there are less than 2 Pets of the specified species in inventory,
        please print a message to the user to let them know.
        Hint: This is the same sorting as Pet's comparator function

        Parameters:
            self
            species: String -- the species you want to breed
            name: String -- the name of the new baby Pet

        Usage Examples:
            >>> ps = PetStore()
            >>> cat = Pet("Cat", "Meowth", 9, "White", 400)
            >>> cat2 = Pet("Cat", "James", 10, "Blue", 100)
            >>> cat3 = Pet("Cat", "Jessie", 10, "Red", 200)
            >>> ps.add_pet(cat)
            >>> ps.add_pet(cat2)
            >>> ps.add_pet(cat3)
            >>> first_pet_list = ps.inventory["Cat"]
            >>> ps.breed("Cat", "Ash")
            >>> second_pet_list = ps.inventory["Cat"]
            >>> baby = Pet("Cat","Ash", 1, "Blue", 500 )
            >>> first_pet_list.append(baby)
            >>> first_pet_list.sort()
            >>> second_pet_list.sort()
            >>> first_pet_list == second_pet_list
            True
        """
```
### `Populate`
This function should be outside of any class, and will be called in your main method.  
```Python
def populate(self, starting_inventory, store):
    """Initializes the pet store with all the animals in the provided
    CSV file.  The CSV file has a column for every parameter in the Pet
    class.  Use each line in the file to create a Pet and then add it to
    the PetStore class's inventory dictionary.

     Parameters:
         self
         starting_inventory: String -- name of a csv file to get data from
         store: PetStore Object -- the pet store to add the inventory to
    """
```
### `Main`

Structure your main method as we have been taught:

```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```

Write a main function that allows the user to run the pet store.  This function should run when this file is run as a script on the command line. 
```sh
python hw3.py
```
The first thing this function should do is instantiate an instance of the Pet Store class.  Next, check the command line arguments passed in on the command line.  If there is no file passed in as an argument, or the file provided does not exist in the current directory, please print a message to the console asking the user to run the script again with a valid file name and exit without throwing an error.

Here's a snippet of code that checks for the existence of a file:

```Python
import os.path
os.path.exists("file_name.txt") # returns True if file_name.txt exists
```

Once you have a valid file name, call populate, passing in this file name and the pet store you just instantiated as the parameters.  
After the populate function is run the user should be able to call any of the functions of the pet store class, as well as be able to print out all the pets in the store and the amount of money the store has at any time. The commands that the user may enter are as follows:
- sellC: calls sell_cheapest, then prints a confirmation message
- sellA: calls sell_all, then prints a confirmation message
- discount: calls discout, then prints a confirmation message
- breed: calls breed, then prints a confirmation message
- inventory: prints out the pet store inventory grouped by species
- money: prints out the stores money
- quit: exits the program gracefully

The first 4 of these commands take in a species as a parameter, so after the user calls one of those functions, the main method should prompt the user for which species they would like to perform the action on.  When breed is called, you should prompt the user for a name for the new baby.  

```
>>> Welcome to your pet store! What would you like to do? sellC
>>> What species would you like to sell? Cat
The cheapest Cat was sold!
>>> Welcome to your pet store! What would you like to do? sellA
>>> What species would you like to sell? Dog
All Dog's were sold!
>>> Welcome to your pet store! What would you like to do? discount
>>> What species would you like to discount? Snake
Snake's are now half off!
>>> Welcome to your pet store! What would you like to do? breed
>>> What species would you like to breed? Bird
>>> What would you like to name this babe Bird? James
Baby James was added to your inventory!
>>> Welcome to your pet store! What would you like to do? money
Your Pet Store has $2100!
>>> Welcome to your pet store! What would you like to do? inventory
Bird:
Species: Bird, Name: Larry, Age: 56, Color: Red, Price: 400
Species: Bird, Name: Emma, Age: 18, Color: Blue, Price: 400
Species: Bird, Name: Leia, Age: 42, Color: Green, Price: 450
-----------------------------------

Cat:
Species: Cat, Name: James, Age: 2, Color: Orange, Price: 200
Species: Cat, Name: Kathy, Age: 4, Color: White, Price: 215
Species: Cat, Name: Laura, Age: 3, Color: Black, Price: 600
-----------------------------------

Dog:
Species: Dog, Name: Alex, Age: 4, Color: Gold, Price: 150
Species: Dog, Name: Todd, Age: 8, Color: Brown, Price: 100
Species: Dog, Name: Gaston, Age: 7, Color: White, Price: 125
-----------------------------------

Snake:
Species: Snake, Name: Draco, Age: 11, Color: Gray, Price: 20
Species: Snake, Name: Pansey, Age: 7, Color: Brown, Price: 75
Species: Snake, Name: Vincent , Age: 9, Color: Silver, Price: 900
Species: Snake, Name: Albert, Age: 11, Color: Tan, Price: 78
-----------------------------------
>>> Welcome to your pet store! What would you like to do? quit
Bye!
```


## Submission Instructions

Attach your `hw3.py` file to your T-Square HW2 assignment submission.

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
