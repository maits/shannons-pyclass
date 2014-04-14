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
	


	for state in states:
	
		new_file.write("\t <tr><td colspan='2'>{1}</td></tr><tr><td>Rank: {0}</td><td> Percent: {4}% </td></tr><tr><td> US House Members: {3}</td><td>Population: {2}</td></tr>".format(state[1], state[0], state[4], state[3], state[2]))

	new_file.write("</table>")

##this doesn't work. It says that the list is out of range. I also need to pop the header



#I took this code from Morgana's Github

with open('state_info.csv', 'r') as states_file:
    states = states_file.read().split("\n")
    for index, state in enumerate(states[1:]): ##Adding the [1:] removes the header boxes
        states[index] = state.split(",")

html_table="""
<table border="1">
<tr>
<td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Rank: {1} </td>
 <td> Percent: {2}% </td>
 </tr>
 <tr>
 <td> US House Members: {3} </td>
 <td> Population: {4} </td>
 </tr>
 </table>
"""

with open('states_info_full.html', 'w') as population_file:
    population_file.write("<select_name=\state\>\n")
    for index, info in enumerate(states[1:]): ##Adding the [1:] removes the header boxes
        population_file.write(html_table.format(states[index][0],states[index][1],states[index][4],states[index][3],states[index][2]))
    population_file.write("</select>")
    
 
#when I run it it says that the list index is out of range. After googling a lot, this is the best explanation I found:
#http://www.daniweb.com/software-development/python/threads/88437/list-index-out-of-range


	
