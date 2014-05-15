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

#I need to check the last part - http://stackoverflow.com/questions/6462949/how-do-you-find-imdb-movie-id
#other useful links: https://github.com/ElizabethAB/PlaytimeExercises/blob/master/lesson05_firstapi.py
#http://bechdeltest.com/api/v1/doc
