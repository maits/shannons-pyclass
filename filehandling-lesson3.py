#this reads the file and prints it

with open("states.txt", "r") as states_file:
	states = states_file.read()

print states

#this reads the file and gives us the file contents as a string. 
#If we have a string, we can turn it into a list!


with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

print states 


#Here, we're splitting the file into a list at each line, 
#and then individually splitting each line into a list by the commas.


with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

	for index, state in enumerate(states):
		states[index] = state.split(",")

print states 
