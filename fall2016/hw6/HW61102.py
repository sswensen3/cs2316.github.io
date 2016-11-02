import requests
import json
import csv
import time
from pprint import pprint


base_url = "https://api.themoviedb.org/3"
API_key = "07bde3797b2ebc9085fbf408483dba80"
sleep_time = 1 / 10


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

    func_url = "/person/{}".format(actor_id)
    payloads = {"api_key": API_key}

    time.sleep(sleep_time)
    response = requests.get(base_url+func_url, params = payloads)
    data = json.loads(response.text)

    actor_name = data.get("name", None)

    return actor_name


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

    func_url = "/person/{}/movie_credits".format(actor_id)
    payloads = {"api_key": API_key}

    time.sleep(sleep_time)
    response = requests.get(base_url+func_url, params = payloads)
    data = json.loads(response.text)

    movie_list = data.get("cast", [])
    movies = {}

    for movie in movie_list:
        movie_id = movie["id"]
        movie_name = movie["title"]
        movies[movie_id] = {
            "name": movie_name,
            "parent": actor_id
        }

    return movies


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

    func_url = "/movie/{}/credits".format(movie_id)
    payloads = {"api_key": API_key}

    time.sleep(sleep_time)
    response = requests.get(base_url+func_url, params = payloads)
    data = json.loads(response.text)

    cast_list = data.get("cast", [])
    cast_members = {}

    for member in cast_list:
        cast_id = member["id"]
        cast_name = member["name"]
        cast_members[cast_id] = {
            "name": cast_name,
            "parent": movie_id
        }

    # pprint(cast_members)
    return cast_members


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

    start_time = time.time()
    costars = {}

    movies = req_movies_for_actor(from_actor_id)
    for movie_id, movie_name in movies.items():
        costar_dict = req_actors_for_movie(movie_id)
        costars.update(costar_dict)

    del costars[from_actor_id]
    return (movies, costars)


def main(args):
    n_args = len(args)

    csv_out = None
    if n_args > 2:
        # try:
        filename = args[2]
        f_out = open(filename, 'w', newline = "")
        csv_out = csv.writer(f_out)
        # except:
            # print("{} is not a valid filename. ".format(args[2]) + \
            #     "Exiting program.")
            # return None

    if n_args > 1:
        try:
            actor_id = int(args[1])
        except:
            print("{} is not a valid value for the actor ID. ".format(args[1]) + \
                "Exiting program.")
            return None
    else:
        running = True
        while running:
            user_inp = input("Would you like to play " + \
                "One Degree from Kevin Bacon? ").lower()[:1]
            if "y" in user_inp:
                actor_id = 4724
                running = False
            elif "n" in user_inp:
                print("No worries. Catch you later.")
                return None
            else:
                print("Yes or no: ", end = "")

    actor_name = lookup_actor_name_by_id(actor_id)
    if actor_name is None:
        print("ID {} is not in the database. ".format(actor_id) + \
            "Exiting program.")

    movies, costars = one_deg_from_actor(actor_id)

    for costar_id, costar_info in costars.items():
        costar_name = costar_info["name"]
        movie_id = costar_info["parent"]
        movie_info = movies[movie_id]
        movie_name = movie_info["name"]
        path = (actor_name, movie_name, costar_name)
        if csv_out:
            csv_out.writerow(path)
        else:
            output_str = "{} > {} > {}"
            print(output_str.format(*path))

    if csv_out:
        print("Output to {} file".format(filename))
        f_out.close()

    return None


print("If testing for Kevin Bacon, this should take less than 60 seconds.")
start_time = time.time()
if __name__ == "__main__":
    import sys
    main(sys.argv)
end_time = time.time() - start_time
print("Took {:.1f} seconds".format(end_time))












