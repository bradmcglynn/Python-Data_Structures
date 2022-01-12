"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Brad McGlynn
ID:      999999999
Email:   bmcglyn4@uwo.ca
Section: CP164 
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)
    
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    line = line.strip()
    listy = line.split("|")
    title = listy[0]
    year = int(listy[1])
    director = listy[2]
    rating = float(listy[3])
    listy2 = listy[4].split(",")
    genres = []
    for el in listy2:
        genres.append(int(el))
    
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """
    movies = []
    fv.seek(0)
    line = fv.readline()
    while line!="":
        line = line.strip()
        movie = read_movie(line)
        movies.append(movie)
        line = fv.readline()
    
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    entry = " "
    valid = False
    print("Genres")
    print(Movie.genres_menu())
    while entry != "" or not valid:
        entry = input("Enter a genre number (ENTER to quit): ")
        if entry:
            if entry.isnumeric():
                if int(entry)>=0:
                    if int(entry) <len(Movie.GENRES):
                        if int(entry) not in genres:
                            genres.append(int(entry))
                            valid = True
                        else:
                            print("Error: genre already chosen.")
                            valid = False
                    else:
                        print("Error: input must be < {}".format(len(Movie.GENRES)))
                        valid = False
                else:
                    print("Error: not a positive number.")
                    valid = False
            else:
                print("Error: not a positive number.")
                valid = False
        else:
            valid = True
        if not genres:
            valid = False
    genres.sort()
    return genres               



def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    for movie in movies:
        if movie.year==year:
            ymovies.append(movie)
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies = []
    for movie in movies:
        if movie.rating>=rating:
            rmovies.append(movie)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    for movie in movies:
        if genre in movie.genres:
            gmovies.append(movie)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    if genres:
        for movie in movies:
            rejected = True
            if len(genres) == len(movie.genres):
                rejected = False
                for genre in genres:
                    if genre not in movie.genres:
                        rejected = True
            if not rejected:
                gmovies.append(movie)
    return gmovies

        
        
        
        
        
        
#         for movie in movies:
#             accepted = False
#             a_remember = True
#             if genres[0] in movie.genres:
#                 for genre in genres:
#                     if genre in movie.genres:
#                         accepted = True
#                     else:
#                         a_remember = False
#             if accepted and a_remember:   
#                 gmovies.append(movie)
#         mcount = len(gmovies)-1
#         if len(genres)>1:
#             while mcount>0:
#                 for genre_i in range(1, len(genres)-1):
#                     if genres[genre_i] not in gmovies[mcount].genres:
#                         gmovies.remove(gmovies[mcount])
#                 mcount = mcount-1


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []
    for code in range(len(Movie.GENRES)-1):
        count = 0
        for movie in movies:
            if code in movie.genres:
                count+=1
        counts.append(count)
    
    return counts
