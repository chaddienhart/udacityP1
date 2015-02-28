'''
author: Chad Dienhart
Feb 15, 2015

Movie is a class to store information about a movie
properties:
title       - The movie title
storyline   - a brief synopsis of the movie
trailer     - the url to the trailer
poster      - a url of the movie's poster image
'''

class Movie(object):
    # define the constructor to take in all property values
    # and initialize the instance
    def __init__(self, title, storyline, trailer, poster):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster

