# Movie-Recommender
Final project of Coursera Course : __[Data Collection with Python](https://www.coursera.org/learn/data-collection-processing-python)__. A movie recommender using TasteDive API and OMDB API.


This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API https://tastedive.com/read/api lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API https://www.omdbapi.com/)



# FUNCTIONS
 1. **extract_movie_titles(name):**
      name, is a string ,representing a movie name.It returns a list of related movies.
 2. **get_related_titles(lst_of_movie):**
      lst_of_movie is a list of movies.The function returns a list of movies related to all the movies in lst_of_movie
 3. **get_movie_data(movie):** 
       movie, is a string, representing a movie name.The function return a dictionary ,which contains all the data about movie.   
 4 . **get_movie_rating(dic_OMDB):**
       dic_OMDB is a dictionary containing information about any movie.The function returns Rotten Tomatoes' rating of the movie as a integer.
 5. **get_sorted_recommendations(lst_of_movies):**
       The function takes a list of movies .It returns a list of recommended movies sorted by Rotten tomatoes ratings
 
     


