---
layout: homework
title: Homework 6
---

# Homework 6: ~~Six~~ One Degree~~s~~ from Kevin Bacon

## Introduction

In this homework you will practice mining data from the internet.

## Problem Description

Many years ago, before the advent of the Google Search, an ancient game was played by the forefathers to test their knowledge of the cinematic arts. One person would simply name an random actor to the player; the player would attempt to connect this random actor with whom they had co-starred in some movie, or with whom that co-star had co-starred in some other movie, and so on... until, within six jumps, the random actor was connected to the almighty cohesive force of the silver screen: Kevin Bacon. 

This game was henceforth known as Six Degrees from Kevin Bacon...

...but this was before the Internet was popular, before the IMDb had its first page, and even before Python was hatched. And it has long been forgotten.

Today, within the span of a few hours, and with the power of Python, the Internets, and our new friend the API, any decent programmer can write a program to start to unravel the mystery that once was: Kevin Bacon.

## Solution Description

### Task 1: Scraping for Bacon

The first stop on this magical journey is to the cybersource of all things movies: the [Internet Movie Database](http://www.imdb.com/), affectionately known as the IMDb. A quick websearch with turn up the webpage entry for Mr. Bacon; but just looking in awe at his filmography is not nearly enough for the task.

We'll need to write a Python function to scrape out all the movies and their names and URLs.

# KATIE! FOR PETE'S SAKE WRITE STUFF HERE!


#### Sub-task 1.5: The Key to Finding More Bacon

Scraping is no fun. Way too many items to inspect. One could iterate through all those movies and find who acts in them, but why bother? It's going to take forever to look at every webpage, write up a script for it, and make sure it doesn't run into any more problems. Instead, let's switch over to using a more powerful tool: **the API**.

While IMDb doesn't have an API available, [themoviedb.org](https://www.themoviedb.org/) does. And like any worthwhile API, it's totally free.

To use it, we'll need two things:
 + get an API key
 + learn how to use the API
 
Luckily, it's easy to do both.
 
##### Getting an API key

First, get an account from [themoviedb.org](https://www.themoviedb.org/). You can sign up [here](https://www.themoviedb.org/account/signup).

Second, sign in and go to your account page. In the left column under your username, there is a link to the API section of your account.

Third, jot down that handy `API Key (v3 auth)` key in a computer file somewhere; you'll need that for later. ***Don't share this key with anyone. No really, don't share it.***

##### themoviedb.org API Documentation

Here's a link to [themoviedb.org API documentation](https://developers.themoviedb.org/3). There is a lot of information there. Probably too much. Bookmark this webpage anyway. You'll need that for later, too.

### Task 2: In The Name of Bacon

Since we're at the [themoviedb.org](https://www.themoviedb.org/) we might as well bring up Kevin's page:  
https://www.themoviedb.org/person/4724-kevin-bacon

See that fancy **4724** in the URL? That's Kevin Bacon's actor ID for [themoviedb.org](https://www.themoviedb.org/). Take a note of that because we're going to need it in our first API function.

Before you do that, it might help to do the following for more insight:

1. Stare at the following page for a bit; it's the documentation for the Get Details API call in the `PEOPLE` section of the API: https://developers.themoviedb.org/3/people
2. After you're done staring, click the `Try it out` tab.
3. Enter your API key (you wrote that down, right?) in the field marked `Your TMDb API key` next to `api_key` in the `Variables` section.
4. Enter **4724** in the `Integer` field next to `person_id` in the `Path Params` section.
5. Click the pinkish `SEND REQUEST` button.

Notice the a URL has popped up (`https://api.themoviedb.org/3/person/4724?api_key=<your_api_key>&language=en-US`), and in the `Response` section below it, there is a response that looks a lot like a nested dictionary\*. If you enter the URL above into your browser (with your API key inserted properly), the webpage will look like that dictionary as well. (\**Note: it's not actually a nested dictionary. It's a JSON object, and what that is isn't that important... but it can be converted fairly easily to a dictionary-like object. You'll need to be able to do that if you want to get the name out. Read on.*)

But we don't want to get names by using the web browser. We want to get them in Python using the `requests` module. If you don't know how to use `requests`, check out this documentation: http://docs.python-requests.org/en/master/user/quickstart/#make-a-request. You'll literally only need to read the first three sections (starting with "Make a Request") and skip the parts about POST, PUT, DELETE, HEAD, and OPTIONS. Those are way too much HTML for us.

Once a request has been made, and you've gotten a response -- we'll call it `response` -- you'll need to convert the text output, `response.text`, into the form of a dictionary using the `json` module in Python (Hint: `response.text` is actually a string of the JSON, not a JSON object. Look for the `json` function that deserializes strings.)

This is the most basic of the API requests that can be made.

```python
def lookup_actor_name_by_id(actor_id):
    """Returns an actor's name by taking in the actor's actor_id using the 
    themoviedb.org's API and the requests module and the json module.
    
    Parameters:
    actor_id: int -- the themoviedb.org ID number of an actor

    Return:
    actor_name: str -- the name of the actor associated with the ID
    
    Usage Examples:
    >>> lookup_actor_name_by_id(4724)
    'Kevin Bacon'
    >>> lookup_actor_name_by_id(2963)
    'Nicolas Cage'
    """
```

### Task 3: A Movie for Every Bacon, A Bacon for Every Movie

Now that we're able to collect the name of any actor given their ID (even though the only ID that really matters is Kevin Bacon's), let's put that ID to use.

First, write a function to return all the movies an actor has been cast in.   
Second, let's also get the cast list for all the actors in a given movie.

Hint: The `PEOPLE` section of the API documentation is the right place to start looking for the right API call for the first function. But the API call needed for the second function is in a different section.

```python
def req_movies_for_actor(actor_id):
   """Looks up all the movies in which an actor with actor_id has been casted. 
    Returns the movies as a nested dictionary with the movie_id as the key, and 
    the name of the movie and the actor's ID as values in the nested dictionary.

    Parameters:
    actor_id: int -- the themoviedb.org ID number of an actor

    Return:
    movie_dict: dict --
        where movie_dict ={
            movie_id: {
              "name": movie_name,
              "parent": actor_id
            }}
        and movie_id: int -- the themoviedb.org ID number of the movie
        and movie_name: str -- the name of the movie for the given ID

    Usage Examples:
    >>> movies = req_movies_for_actor(4724)
    >>> "Tremors" in [movie["name"] for movie in movies.values()]
    True
    >>> "Titanic" in [movie["name"] for movie in movies.values()]
    False
    >>> 4724 in [movie["parent"] for movie in movies.values()]
    True
    >>> 2963 in [movie["parent"] for movie in movies.values()]
    False
    """
```

```python
def req_actors_for_movie(movie_id):
    """Looks up all the cast members in the movie with movie_id. Returns the 
    cast as a nested dictionary with the cacst_id as the key, and the name of 
    the cast member and the movie's ID as values in the nested dictionary.
    
    Parameters:
    movie_id: int -- the themoviedb.org ID number of a movie

    Return:
    cast_dict = dict --
        where cast_dict = {
            cast_id: {
                "name": cast_name,
                "parent": movie_id
            }}
        and cast_id: int -- the themoviedb.org ID number of an actor
        and cast_name: str -- the name of the cast member for the given ID

    Usage Examples:
    >>> cast_members = req_actors_for_movie(9362)
    >>> 'Kevin Bacon' in [cast["name"] for cast in cast_members.values()]
    True
    >>> 'Nicolas Cage' in [cast["name"] for cast in cast_members.values()]
    False
    >>> 9362 in [cast["parent"] for cast in cast_members.values()]
    True
    >>> 597 in [cast["parent"] for cast in cast_members.values()]
    False
    """
```

### Task 4: First Degree Baconry

Now that there's a way to see what movies an actor has been cast in, and a way to see what actors have worked in a given movie, now we need a function to combine it.

Write a function that looks up all of the--

**Wait! Before you do that, you need to know something!**  
Folks who run APIs know that web scrapers like yourself love to query their APIs constantly. In fact, if web scrapers had it their way, they'd try to eat up all the bandwidth of the website running the API.

To combat the web scrapers, the API admins at [themoviedb.org](https://www.themoviedb.org/) have set a limit of 40 requests in 10 seconds. 

If you make 41 requests before the 10 seconds is up, they send you a fake response that says:  
`{"status_code":25,"status_message":"Your request count (41) is over the allowed limit of 40."}`   
You might not even know it unless you check the response! That means you might not know if a fake request was sent for a given movie!

To combat the API admins and avoid getting a fake response, we'll need to put a delay on the requests so that the request timer can reset after 10 seconds. To make Python delay its next command for 60 sec, you could use this code:

```python
import time
time.sleep(60)
```

However, waiting for 60 seconds between requests takes a really a long time. Figure out a good amount of time to delay between requests. Points off if your entire code takes more than 1 minute to run, when we run this for Kevin Bacon! We'll be checking!

Okay, now without any further delay...

Write a function that looks up all of the movies of a given actor, and then finds their co-stars for all those movies together. Oh yeah, don't include the starting actor with result all of their co-stars. It's not like they're staring in a movie with themselves.

```python
def one_deg_from_actor(from_actor_id):
    """Looks up all the co-stars for an actor with from_actor_id. Returns a 
    tuple with a nested dictionary of all the movies by id with their names and 
    parent actor (as in req_movies_for_actor) and a nested dictionary of all the
    costars by id with their names and parent movie (as in 
    req_actors_for_movie), excluding the from_actor_id themselves.

    Parameters:
    movie_id: int -- the themoviedb.org ID number of a movie

    Return:
    (movies, costars): tuple --
        where movies = {
            movie_id:{
                "name": movie_name,
                "parent": from_actor_id}}
        and costars = {
            costar_id:{
                "name": costar_name,
                "parent": movie_id}}
    
    Usage Examples:
    >>> start_time = time.time()
    >>> bacon_movies, bacon_costars = one_deg_from_actor(4724) # this should take less than 60 secs
    >>> end_time = time.time() - start_time
    >>> end_time < 60
    True
    >>> len(bacon_movies)
    72
    >>> len(bacon_costars)
    1031
    >>> bacon_costars.get(4724, None) == None
    True
    """
```

### Task 5: Bringing Home the Bacon

Finally, we'll want a main function that wraps up what was done above, and we want it work for any actor... although mostly for Kevin Bacon.

In this one particular case, it's useful to write `API_KEY = <your api key>` as a *global variable* near the top of your script. But **don't leave it in your code during submission**.

Also, we've put a timer around the `if __name__ == "__main__"` statement so that you can see how much time your code took to execute.

```python 
# your name
# your GTID#

# import all the modules

API_KEY =  # enter your API key from sub-task 1.5 as a global variable
## SUPER IMPORTANT! Delete your API key before submitting homework!
## You'll need it to test your code, but it's literally your key, not ours.
## -20 points if you don't delete it before submission.

# write all the helper functions

def main(args):
   """Write your docstring here."""
   # Write your code here.


print("If testing for Kevin Bacon, this should take less than 60 seconds.")
start_time = time.time()
if __name__ == "__main__":
    import sys
    main(sys.argv)
end_time = time.time() - start_time
print("Took {:.1f} seconds".format(end_time))
```

#### `main()` Function Requirements

1. Handle up to two additional arguments (excluding the script name itself, i.e. `args[0]`).
2. The first additional argument (i.e. `args[1]`) is *optional*. It's the `actor_id`, according to [themoviedb.org](https://www.themoviedb.org/).
  + If the `actor_id` is given, it should be an `int` and it needs to be used to search [themoviedb.org](https://www.themoviedb.org/)'s API. 
    + If the `actor_id` argument is invalid or the actor does not exist, print an error and quit.
  + If the `actor_id` is *not* given, ask if the user wants to play One Degree from Kevin Bacon. 
    + If they do, run the program using Kevin Bacon's ID and print the output to console. 
    + If they don't, print a parting message and quit.
3. The second additional argument is *optional*. It's the filename for a `.csv` file.
  + If a filename is given, write a `.csv` file where each row is the link between that actor and everyone they have co-starred with including the movie they co-starred in. Each row in the `.csv` file should have the form `"actor_name,movie_name,costar_name\n"`. Also, print a message to the console showing the file was written properly. See example below.
     + If the filename argument is not valid, print an error and quit.
  + If a filename is *not* given, print the linking path between that actor and everyone that actor has co-starred with, including the movie they co-starred in. The form of the print out should be `actor_name > movie_name > costar_name`. See example below.

#### Examples

##### Example 1: Writes to File

The following command...

```
$ python hw6.py 1117334 output.csv
If testing for Kevin Bacon, this should take less than 60 seconds.
Writing data to output.csv file... done.
Took <however many> seconds.
```

...writes to `output.csv` with the following text in some order:

```
Briggs Branning,Bottle Rocket,Elissa Sommerfield
Briggs Branning,Bottle Rocket,Isiah Ellis
Briggs Branning,Bottle Rocket,Luke Wilson
Briggs Branning,Bottle Rocket,Owen Wilson
Briggs Branning,Bottle Rocket,Robert Musgrave
Briggs Branning,Bottle Rocket,Temple Nash
```

##### Example 2: Prints to Console

This command prints the following to the console, in some order.

```
$ python hw6.py 1117334
If testing for Kevin Bacon, this should take less than 60 seconds.
Briggs Branning > Bottle Rocket > Elissa Sommerfield
Briggs Branning > Bottle Rocket > Isiah Ellis
Briggs Branning > Bottle Rocket > Luke Wilson
Briggs Branning > Bottle Rocket > Owen Wilson
Briggs Branning > Bottle Rocket > Robert Musgrave
Briggs Branning > Bottle Rocket > Temple Nash
Took <however many> seconds.
```

##### Example 3: No Arguments

This command prints something like the following to the console. The prompt statement can be worded as you like.

```
$ python hw6.py
If testing for Kevin Bacon, this should take less than 60 seconds.
No actor chosen. Do you want to play one degree from the default chosen one, Kevin Bacon? 
<if yes, prints output to console; this line not actually printed>
<if no, prints parting message>
Took <however many> seconds.
```

##### Example 4: Invalid Arguments

These commands print something like the following. The error message should reflect the error.

```
$ python hw6.py 12345678901234567890
If testing for Kevin Bacon, this should take less than 60 seconds.
ERROR: We've don't recognize that id. They're obviously not connected to Kevin Bacon or anyone else 
for that matter. Please play again.
Took <however many> seconds.
```

```
$ python hw6.py 4724 :@#*&$!
If testing for Kevin Bacon, this should take less than 60 seconds.
ERROR: Whoa, buddy! We can't write to files like that. Try again, and please try to keep it clean.
Took <however many> seconds.
```

## Submission Instructions

- [ ] Attach your `hw6.py` file to your T-Square HW6 assignment submission.
- [ ] ***Delete your API key, or else!*** Every API key is a unique snowflake generated uniquely for your account. You should never share your API keys to anyone else, including your instructor, your TA, your aunt Sally, your roommate, your roommate's dog, your future mother-in-law, my ex-girlfriend or anyone else who could possibly begin to harbor a grudge (except your TAs and instructors; we'll don't know even know what grudges are). We don't want your key. We don't want the responsiblilty of having it. Don't submit it with your homework. Delete it as a global variable when you're ready to submit your homework. -20 points to anyone who doesn't delete it.
- [ ] ***Homework 6 submissions should run without syntax or runtime errors!*** Non-compiling code will receive a 0. Be sure to follow the instructions below to verify that files are submitted correctly and the code works when you run it.

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
