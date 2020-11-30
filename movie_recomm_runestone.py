#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist.
#The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media.
#It will be a python dictionary with just one key, ‘Similar’.




import requests_with_caching
import json
import re   

def get_movies_from_tastedive(name):
    params = {'q' : name, 'type' : 'movies', 'limit' : 5}
    resTD = requests_with_caching.get('https://tastedive.com/api/similar',params = params)
    resTD_py = resTD.json()
    return resTD_py



#Write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.


def extract_movie_titles(dict_movies):
    movie_lst =[movie['Name'] for movie in dict_movies['Similar']['Results']]
    return movie_lst
    

#Write a function, called get_related_titles. It takes a list of movie titles as input.
#It gets five related movies for each from TasteDive, extracts the titles for all of them,
#and combines them all into a single list. Don’t include the same movie twice.



def get_related_titles(lst_of_movie):
    """Returns a list of movies , realated to the movies in the list lst_of_movie"""
    related_title_lst = []
    for movie in lst_of_movie:
        related_movie = extract_movie_titles(get_movies_from_tastedive(movie))
        for title in related_movie :
            if title not in related_title_lst:
                related_title_lst.append(title)
    return related_title_lst


#Define a function called get_movie_data. It takes in one parameter which is a string that should
#represent the title of a movie you want to search. The function should return a dictionary with information about that movie.


def get_movie_data(movie):
    OmdbUrl = 'http://www.omdbapi.com/'
    param = {'t' : movie, 'r' : 'json'}
    resOMDB = requests_with_caching.get(OmdbUrl, params = param)
    resPY = resOMDB.json()
    return resPY
    

#write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts
#the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”,
#it would return 97. If there is no Rotten Tomatoes rating, return 0.



def get_movie_rating(dic_OMDB):
    for ratings in dic_OMDB['Ratings']:
         if ratings['Source'] == 'Rotten Tomatoes':
            RottenTomatoes_Rating = ratings['Value']
            RottenTomatoes_Rating = re.findall('([0-9.]+)', RottenTomatoes_Rating)   #it will return a list ,like ['94']
            RottenTomatoes_Rating = int(RottenTomatoes_Rating[0])
            return RottenTomatoes_Rating
         else:
            continue
    return 0
    

#Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related
#movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by
#their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.



def get_sorted_recommendations(lst_of_movies):
    movie_Rating_dict = {}
    related_movies = get_related_titles(lst_of_movies)
    for movie in related_movies:
        data = get_movie_data(movie)
        RT_Rating = get_movie_rating(data)
        movie_Rating_dict[movie] = RT_Rating
    sorted_recommendtion = sorted(movie_Rating_dict, key = lambda movie : -movie_Rating_dict[movie],reverse = False)
    return sorted_recommendtion 
   









