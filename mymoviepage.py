import fresh_tomatoes
import movie

# create instances of Movie(title, synopsis, youtube_url, poster_image)
# create one for each of my favorite movies
starwars = movie.Movie("Star Wars", "Use the force", "www.youtube.com/watch?v=9gvqpFbRKtQ", "http://img3.wikia.nocookie.net/__cb20140311211533/starwars/images/a/a9/Ep4_OST.png")
twentyone = movie.Movie("21", "Beating the house at blackjack", "www.youtube.com/watch?v=ZRzZX2aN3I0", "http://upload.wikimedia.org/wikipedia/en/a/a8/21_%282008_film%29.jpg")
matrix = movie.Movie("Matrix", "You are only part of the matrix", "www.youtube.com/watch?v=_Ls19O-9p3s", "https://samtrusler.files.wordpress.com/2009/11/the-matrix-film-poster.jpg")
tisamary = movie.Movie("There's Something About Mary", "Franks and beans, franks and beans", "www.youtube.com/watch?v=eGjXwDYpOLE", "http://ia.media-imdb.com/images/M/MV5BMTAzNzM3NTM4NDNeQTJeQWpwZ15BbWU4MDgzOTgzMTAx._V1_SX640_SY720_.jpg")

# create a list of movie objects and initialize it with my favorites
movies = [starwars, twentyone, matrix, tisamary]

# call the open_movies_page passing in the list of movies
fresh_tomatoes.open_movies_page(movies)

