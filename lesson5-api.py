import requests

title = raw_input('Enter the name of a movie: ')

url = 'http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}'.format(title).replace(" ","+").replace("'","&#39;")

print url

response = requests.get(url).json()

print response

# Goal 1:
#   Ask the user for the movie title they want to check
#   Display all of the details about the movie returned by the API
#
#   Things to keep in mind:
#       How will your program behave when multiple movies are returned?
#       How will your program behave when no movies are returned?
#       How will your program behave with works like "the" in the title?

#the in title
if "the" in title[0:4]:
	title = title.replace("the ", "")
	print title		

#multiple movies
for title in response:
	if title > 1:
		print "Your query returned multiple results. You might want to be more specific."
		break

search = raw_input('Do you want to search again?')
if search == 'yes':
	for title in response:
		print title['title'], title['rating']
if search == 'no':
		print "Cool"

#no movies are returned
for title in response:
	if title == 0:
		print "Your query returned no results. Try again!"
		break


# Goal 2:
#   Check to see if the user input is a movie title or an ImdbID and use the proper endpoint

for title in response:
	if len(title) == 7:
		print "This is a movie ID, not the title."
		bt_title = requests.get('http://bechdeltest.com/api/v1/getMovieByImdbId', params= {'imdbid' : title}).json()
	else:
		bt_title = requests.get('http://bechdeltest.com/api/v1/getMoviesByTitle', params={'title' : title}).json()
		print "This is the movie you're looking for."
		print bt_title

# Goal 3:
# Integrate this with the Open Movie Database API: http://www.omdbapi.com/
#   Display all of the details from both APIs when searching for a movie.
#   Note that you may need to prefix your ImdbIDs with 'tt' to get the search to work.

# Copy these URLs into your browser!
# To visualize as a CSV, copy the JSON into http://konklone.io/json

# Sample Bechdel test API returns: http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid=0367631
# JSON: 
    # {
    #   "visible": "1",
    #   "date": "2009-12-05 05:13:37",
    #   "submitterid": "270",
    #   "rating": "3",
    #   "dubious": "0",
    #   "imdbid": "0367631",
    #   "id": "551",
    #   "title": "D.E.B.S.",
    #   "year": "2004"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488879

# Sample Open Movie Database API returns: http://www.omdbapi.com/?i=tt0367631&t=
# JSON:
    # {
    #   "Title": "D.E.B.S.",
    #   "Year": "2004",
    #   "Rated": "PG-13",
    #   "Released": "25 Mar 2005",
    #   "Runtime": "91 min",
    #   "Genre": "Action, Comedy, Romance",
    #   "Director": "Angela Robinson",
    #   "Writer": "Angela Robinson",
    #   "Actors": "Sara Foster, Jordana Brewster, Meagan Good, Devon Aoki",
    #   "Plot": "Plaid-skirted schoolgirls are groomed by a secret government agency to become the newest members of the elite national-defense group, D.E.B.S.",
    #   "Language": "English",
    #   "Country": "USA",
    #   "Awards": "1 win & 2 nominations.",
    #   "Poster": "http://ia.media-imdb.com/images/M/MV5BMjA0OTU5ODgyOF5BMl5BanBnXkFtZTcwODczNDgyMQ@@._V1_SX300.jpg",
    #   "Metascore": "42",
    #   "imdbRating": "5.2",
    #   "imdbVotes": "10,563",
    #   "imdbID": "tt0367631",
    #   "Type": "movie",
    #   "Response": "True"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488839

#my comments start here
#I need to check the last part - http://stackoverflow.com/questions/6462949/how-do-you-find-imdb-movie-id
#other useful links: https://github.com/ElizabethAB/PlaytimeExercises/blob/master/lesson05_firstapi.py
#http://bechdeltest.com/api/v1/doc
