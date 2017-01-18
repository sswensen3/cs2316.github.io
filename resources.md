---
layout: default
title: CS 2316 - Resources
---

# Resources

## Get Started

Try to do the following before the first day of class.

### 1. Install Python

- **Recommended**: [Miniconda](http://conda.pydata.org/miniconda.html). Be sure to get the Python 3 version! Once you have Miniconda, open your terminal application (or `cmd` on Windows), and enter the following commands (`$` is the command prompt on most Unix shells. It would be something like `C:\>` in Windows's terminal, cmd. You don't type/copy the prompt from shell examples like this.):

```sh
$ conda update conda
$ conda install pymysql flask requests beautifulsoup4 pyqt
$ conda install numpy pandas scipy matplotlib scikit-learn ipython-notebook
```

For this class you don't technically need the third line above, but these are common packages used in data analytics, which is a major application area for Python. We may discuss some of these as special topics during the last week of the course.

- Alternate methods: [Installing Python](installing-python.html) (But, seriously, just use  [Miniconda](http://conda.pydata.org/miniconda.html). It's the best thing to happen to Python package management, well, ever.)

### 2. Check Your Python Installation


1. Open a terminal, i.e., operating system (OS) command shell.

    -  The Mac OS X terminal is `/Applications/Utilities/Terminal.app` in the Finder.  You should drag Terminal to your dock -- you'll use it often.

    - On Windows search for and run `cmd.exe`, for example by simply typing `cmd` in the start search box.

2. At the command prompt type `python3 --version`.  You should get a response like `Python 3.5.2 :: Continuum Analytics, Inc.`.

    - Note: on Windows the Python 3 command is just <code>python</code> (without the 3). Anaconda/Miniconda also aliases `python` to `python3`.

### 3. Choose, install and configure a text editor using our [text editors guide](text-editors.html).

In this class we will use the terminal, the Python REPLs (`python` and `ipython`), and text editors. We will not use an integrated development environment (IDE) such as IDLE or PyCharm. Learning how to use the command line and text editors is crucial to becoming a competent programmer and data manipulator.

## Learn About Programming and Computing

- [Basic Unix](http://matt.might.net/articles/basic-unix/) - a tutorial introduction to the Unix command line
that will give you the basic skills you need for this class should you choose to use a unix-like operating system like Ubuntu Linux or Mac OS X
- [Text Editors](text-editors.html) - an intro to text editors for beginning programmers

## Learn About Python

- Online Python documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
- [Python Style Guide](http://legacy.python.org/dev/peps/pep-0008/)
- Jay Summet's previous [CS 2316 class web sites](http://www.cc.gatech.edu/~summetj/teaching.html#cs2316)

## Enrolled in Modern Physics 2?

If you're enrolled in Modern Physics 2 and need to run VPython for Physics, then you'll need to manage a Python 2 installation for Physics and Python3 for CS 2316. You can manage two Python version using [conda environments](http://conda.pydata.org/docs/using/envs.html). To set it up, do this at the command line:

```sh
conda create -n py27 python=2.7
conda install psutil
source activate py27
conda install -c mwcraig vpython=6.11.0
```

The first two lines create a conda environment for Python 2.7, the third line activates it, and the fourth line installs vpython into your Python 2.7 environment (named py27).

With this setup, any time you want to run vpython you have to do

```sh
source activate p27
```

And when you're done you can go back to the root 3.5 environment for CS 2316 with

```sh
source deactivate
```

### Non-Conda Solution

Some students have reported success installing the Physics VPython software after installing Python 2 from [python.org](https://www.python.org/). With this setup you would use `python` for Physics stuff and `python3` for CS 2316 stuff. At the command line you should get something like this:

```sh
$ python --version
Python 2.7.3
$ python3 --version
Python 3.5.2 :: Continuum Analytics, Inc.
```
