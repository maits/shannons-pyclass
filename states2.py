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

#when I run this code, ot says the index list is out of range.

#I took this coe from Morgana's Github

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








 
