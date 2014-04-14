with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

	print "<select name='States'>"

	for index, state in enumerate(states):
		states[index] = state.split("\t")

	for state in states:
		print "\t <option value='{0}'>{1}</option>".format(state[0], state[1])


print "</select>"

#this code works fine

######

with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

#	print "<select name='States'>"

	for index, state in enumerate(states):
		states[index] = state.split("\t")

	with open("states.html", "w") as new_file:		
		new_file.write("<select name='States'>")


		for state in states:
			new_file.write("\t <option value='{0}'>{1}</option>".format(state[0], state[1]))


		new_file.write("</select>")








 
