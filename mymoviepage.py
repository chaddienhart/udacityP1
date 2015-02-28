'''
author: Chad Dienhart
Feb 15, 2015

Create instances of Movie for each of my favorite movies.
The title, synopsis, trailer url, and image url need to be provided to create
the Movie object.

Put them in a list and call fresh_tomatoes which will create an
html page with my list of movies and open it in a webbrowser.
'''

import fresh_tomatoes
from movie import Movie

starwars = Movie("Star Wars", "Use the force", "www.youtube.com/watch?v=9gvqpFbRKtQ", "http://img3.wikia.nocookie.net/__cb20140311211533/starwars/images/a/a9/Ep4_OST.png")
twentyone = Movie("21", "Beating the house at blackjack", "www.youtube.com/watch?v=ZRzZX2aN3I0", "http://upload.wikimedia.org/wikipedia/en/a/a8/21_%282008_film%29.jpg")
matrix = Movie("Matrix", "You are only part of the matrix", "www.youtube.com/watch?v=_Ls19O-9p3s", "https://samtrusler.files.wordpress.com/2009/11/the-matrix-film-poster.jpg")
tisamary = Movie("There's Something About Mary", "Franks and beans, franks and beans", "www.youtube.com/watch?v=eGjXwDYpOLE", "http://ia.media-imdb.com/images/M/MV5BMTAzNzM3NTM4NDNeQTJeQWpwZ15BbWU4MDgzOTgzMTAx._V1_SX640_SY720_.jpg")
pulpfiction = Movie("Pulp Fiction", "You sending The Wolf?", "www.youtube.com/watch?v=wZBfmBvvotE", "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg")

# create a list of movie objects and initialize it with my favorites
movies = [starwars, twentyone, matrix, tisamary, pulpfiction]

# call the open_movies_page passing in the list of movies
# the order of the list is the order they will be displayed
fresh_tomatoes.open_movies_page(movies)

