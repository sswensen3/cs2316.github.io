---
layout: homework
title: Homework 5 - DoctorBase
---

# Homework 5 - DoctorBase

## Introduction

A common task in data management systems is receiving data from an external system in XML files and storing it in a relational database. Python includes libraries for easily reading XML files and interacting with databases. We store data in databases for record keeping and so that we can answer questions about the data.

In this assignment you will

- create a SQLite database using provided database creation scripts,
- write a Python program that parses an XML data file and inserts the data from it into the database, and
- create a SQL script with queries to answer questions about data in the database.

# Problem Description

You're starting a new job as a database manager at the Centers for Disease Control (CDC). In this role you need to manage and analyze data about doctors and patient care. You receive doctor data from outside sources in the form of XML files which you need to insert into your database, and you use the database to answer questions about the data.

# Solution Description

You'll store data in a SQLite database and import data from XML files using a Python script.

### Preparing Your Database (10 points)

You've been provided with two database scripts to create the database and populate it with data (download [`doctors-schema.sql`](doctors-schema.sql) and [`doctors-data.sql`](doctors-data.sql). Run `sqlite3` with the database file name `doctors.db` as an argument and run your database creation and population scripts on this database.  This will look something like:

```sh
$ sqlite3 doctors.db
SQLite version 3.7.9 2011-11-01 00:52:41
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .read doctors-schema.sql
sqlite> .read doctors-data.sql
sqlite> .exit
```

After the session above the current directory will have a file called `doctors.db` with populated tables.

## Importing XML Data into a Database

Write a Python script named `import_doctors.py` that reads an XML file named in the first command-line argument to your program and inserts the doctor data contained in the XML file into the `doctor` table of the database specified as the second command-line argument to your script.  Test your program on the database you created in the previous step.  You should develop your program in stages, described in the sections below.

### Inserting Doctors (40 points)

Your script should have a function with the signature `insert(conn, first_name, last_name, specialty)` that inserts a single doctor record into the database represented by the [connection](https://docs.python.org/3/library/sqlite3.html?highlight=connection\#connection-objects) object `conn`.  Remember to commit your changes to the database so they are saved in the database file.

### Extracting Elements from doctors.xml (30 points)

Your script's main block should parse an XML file with the same structure as [`doctors.xml`](doctors.xml) using Python's `xml.etree.ElementTree` parser or [xmltodict](https://github.com/martinblech/xmltodict).

If you choose to use `ElementTree`: with the tree that `ElementTree.parse()` returns your program should:

1. find all the `doctor` elements
2. for each `doctor` element
  - extract the firstName, secondName, and specialty element text
  - call `insert(conn, first_name, last_name, specialty)`
    with the data from the elements above

If you choose to use `xmltodict` you will simply be processing a Python dictionary.

### Querying a Database (30 points)

Write a SQL script, `query-doctors.sql`, that includes queries to answer the following questions:

- What are the first names and last names of the patients who have cardiologists for primary care providers (PCP)?
- What are the first names and last names of the patients who saw their doctor (PCP) in May 2010?
- OPTIONAL BONUS (5 points): What are the first name and last name of the doctor who has the most patients (not the most visits)?
- OPTIONAL BONUS (5 points): What are the first names and last names of the doctors who have no patients (not visits)?


Your `query-doctors.sql` should contain only the `SELECT` queries requested above.

## Tips

- Your `import_doctors.py` should look like the example program we wrote in class.
- Review the [example SQL code](../../code/databases) on the course web site.
- SQLite doesn't have a datetime data type, so you have two options: Julian day, or text.  The simplest approach is using the `text` type for your datetime column and storing datetime values using [the subest of ISO 8601 used by internet applications](http://www.w3.org/TR/NOTE-datetime).  For example, the text representing 11:55pm on 26 June 2014 would be `2014-06-26T23:55`.  Can you think of an advantage of formatting datetime strings like this?
- If you use the datetime format suggested above, you can match parts of a field using the `LIKE` or `GLOB` SQL operators.  For example, to find all the rows in `visit` that occurred in March 2005, you could use ` select * from visit where date like '2005-03-%';` or `select * from visit where date glob '2005-03-*';`


## Turn-in Procedure

Submit your `import_doctors.py`, `query-doctors.sql` and `doctors.db` files on T-Square as attachments.  When you're ready, double-check that you have submitted and not just saved a draft.

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
