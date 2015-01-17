# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

var_bread = input("How many slices of bread do you have?")
var_peanutbutter = input("How many sandwiches worth of peanut butter do you have?")
var_jelly = input ("How many sandwiches worth of jelly do you have?")


if var_bread == 2 and var_peanutbutter == 1 and var_jelly == 1:

	print "You can make a peanut butter and jelly sandwich!" 

else:
	print "Looks like you don't have a lunch today"

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make


if var_bread >= 2 and var_peanutbutter >= 1 and var_jelly >= 1:
	total = var_bread / 2

if var_peanutbutter < total:
        total = var_peanutbutter

if var_jelly < total:
        total = var_jelly

	print "You can make {0} sandwiches".format(total)

else:
	print "Looks like you don't have a lunch today"



# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

if var_bread % 2 != 0 and var_peanutbutter %2 != 0:

	print "You can make an open-face sandwich, too"

else:
	print "Looks like you don't have a lunch today"

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
#Continue from the third goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

#when I tried this, it didn't work unless I entered all the variables before each if statement, not just the one I was trying to test

if var_bread < 2  and var_peanutbutter == 1 and var_jelly == 1: 

	print "You need more bread"

else: 
	print "You can make a peanut butter and jelly sandwich!" 


if var_bread == 2  and var_peanutbutter < 1 and var_jelly == 1: 

	print "You need more peanut butter"

else:
	print "You can make a peanut butter and jelly sandwich!" 

if var_bread == 2  and var_peanutbutter == 1 and var_jelly < 1: 

	print "You need more jelly"

else:
	print "You can make a peanut butter and jelly sandwich!" 

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

if var_bread == 2  and var_peanutbutter == 1 and var_jelly == 0: 

	print "You can still make a peanut butter sandwich but you should take a hard, honest look at your life"

else:

	print "You're fine"
