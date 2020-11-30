# THIS CODE WILL WORK ONLY IN FULL PYTHON ENVIRONMENT.
#FOR CODE ,WHICH WILL WORK IN RUNESTONE ENVIRONMENT SEE movie_recomm_runestone.py



import requests
import json
import re


def extract_movie_titles(name):    #input is a string
    """Extract movie's title related to the movie entered i.e name"""
    baseURL = 'https://tastedive.com/api/similar'
    params = {'q' : name, 'type' : 'movie', 'limit' : 5, 'k' : 'your key'}
    respTD = requests.get(baseURL, params = params)
    res_Py = respTD.json()
    return [recom['Name'] for recom in res_Py['Similar']['Results']]


def get_related_titles(lst_of_movie):
    """Returns a list of movies , realated to the movies in the list lst_of_movie"""
    related_title_lst = []
    for movie in lst_of_movie:
        related_movie = extract_movie_titles(movie)
        for title in related_movie :
            if title not in related_title_lst:
                related_title_lst.append(title)
    return related_title_lst



def get_movie_data(movie):
    OmdbUrl = 'http://www.omdbapi.com/'
    param = {'apikey' : 'your api key', 't' : movie, 'r' : 'json', 'type' : 'movie'}
    resOMDB = requests.get(OmdbUrl, params = param)
    resPY = resOMDB.json()
    return resPY
    
    

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
     
        
 def get_sorted_recommendations(lst_of_movies):
    movie_Rating_dict = {}
    related_movies = get_related_titles(lst_of_movies)
    for movie in related_movies:
        data = get_movie_data(movie)
        RT_Rating = get_movie_rating(data)
        movie_Rating_dict[movie] = RT_Rating
    sorted_recommendtion = sorted(movie_Rating_dict, key = lambda movie : movie_Rating_dict[movie], reverse = True )
    return sorted_recommendtion 
        
        
   print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
    
   

