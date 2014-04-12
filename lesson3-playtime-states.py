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

#Challenge 3 and 4

with open("state_info.csv", "r") as states_file:
	states = states_file.read().split("\n")

#	print states

	for index, state in enumerate(states):
		states[index] = state.split("\t")

#	print states

	with open("states1.html", "w") as new_file:		
		new_file.write("<table border='1'>")
		

#
		for state in states:
	
			new_file.write("\t <tr><td colspan='2'>{1}</td></tr><tr><td>Rank: {0}</td><td> Percent: {4}% </td></tr><tr><td> US House Members: {3}</td><td>Population: {2}</td></tr>".format(state[1], state[0], state[4], state[3], state[2]))

		new_file.write("</table>")

##this doesn't work. It says that the list is out of range. I also need to pop the header/ 
