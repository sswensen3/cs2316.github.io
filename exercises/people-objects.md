---
layout: exercise
title: Treating People as Objects
---

# Exercise: Treating People as Objects

## Introduction

In this exercise you will practice defining and using classes, and performing simple manipulations of collections of objects.

## Problem Description

You need to view some data about people in various ways.

## Solution Description

The [`people.py`](people.py) has starter code that creates `Person` objects in a list `peeps`. In the [`people.py`](people.py) file:

- Write a `Person` class with:

  - an `__init__` method that takes:
    - a name,
    - a birthdate for matted in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format,
    - a height in cm,
    - a weight in kilograms,
  - a `__repr__` method that returns the `name` field;


  - a `height_inches` method that returns the `Person` object's height in inches, and
  - a `weight_pounds` method that returns the `Person` object's weight in pounds.

- Write an expression that assigns to `avg_height` the average height of the `Person` objects in `peeps`.

- Write an expression that assigns to `avg_weight` the average weight of the `Person` objects in `peeps`.

- Bonus: write a function, `avg_by`, that takes a sequence of `Person` objects and a `key` function to take the average of, similar to the `key` function of `sorted`.

- Write an expression that assigns to `name2height` a Dict[str, int] that maps `Person` names to their heights.

- Write an expression that assigns to `name2weight` a Dict[str, int] that maps `Person` names to their weights.

- Bonus: write a function, `dict_builder`, that takes a list of ojects and a  `key_val` function that takes a single parameter that is an element of the list, and returns a tuple that becomes a key-value mapping in a dict returned by `dict_builder`.

- Write an expression that assigns to `by_age` a list of `Person` objects in `peeps` sorted in aschending order by age.