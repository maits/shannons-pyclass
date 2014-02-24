pbj-sandwich-part2
==================

Second part of the pbj sandwich exercise 

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

bread = input("How many slices of bread do you have?")
peanutbutter = input("How much peanut butter do you have?")
jelly = input ("How much jelly do you have?")

#I couldn't start sandwich at 0 because it started counting at 0 then. So I had to start sandwich at 1 and then substract 1 in the second output.

sandwich = 1

while bread >= 2 and peanutbutter >=1 and jelly >=1:
	print "I'm making sandwich #{0}".format(sandwich)

	bread = bread - 2

	peanutbutter = peanutbutter - 1
	jelly = jelly - 1 
	sandwich = sandwich + 1

print "All done; only had enough bread for {0} sandwiches.".format(sandwich - 1)

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread = input("How many slices of bread do you have?")
peanutbutter = input("How much peanut butter do you have?")
jelly = input ("How much jelly do you have?")


sandwich = 1

while bread >= 2 and peanutbutter >=1 and jelly >=1:
	print "I'm making sandwich #{0}".format(sandwich)
	bread = bread - 2
	peanutbutter = peanutbutter - 1
	jelly = jelly - 1 
	sandwich = sandwich + 1

	if bread >=1 and peanutbutter > 0 and jelly > 0:
		print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread/2, peanutbutter, jelly)

	if jelly == 0:
		print "All done; I ran out of jelly"
	if peanutbutter == 0:
		print "All done; I ran out of peanutbutter"
	if bread <= 1:
		print "All done; I ran out of bread" 


