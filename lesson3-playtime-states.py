#Challenge 1 & 2

with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

#	print "<select name='States'>"

	for index, state in enumerate(states):
		states[index] = state.split("\t")

	with open("states.html", "w") as new_file:		
		new_file.write("<select>")

		for state in states:
	
			new_file.write("\t <option value='{0}'>{1}</option>".format(state[0], state[1]))


		new_file.write("</select>")

#this creates a drop-down menu with each state next to the other one. Not necessary, but since I had it, didn't want to delete it.

	#	for state in states:
	#		new_file.write('<select><option value="state_abbreviation">{0}</option>'.format(state[1]))

	#	new_file.write("</select>")

#this is the html template from states ex2 I used to write this one

#StateNames = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
#StateAbbreviations = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

#print '<select>'
#for StateAbbreviation, StateName in zip(StateAbbreviations, StateNames):
#	print '\t<option value="{0}">{1}</option>'.format(StateAbbreviation, StateName)
#print '</select>'

#for state in states:
#	print '<select><option value="state_abbreviation">'
#	print state
#	print '</option></select>'

#this doesn't work. It says that list is out of range. I need to pop the headers and fix the split 
