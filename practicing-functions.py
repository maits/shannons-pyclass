#lesson 4 - slide 16

#Create a function that will return a string containing 'Hello, <name>!' 
#So when you call the function like this: 
#print greeting('Shannon') 
#This should happen in response: 

#Hello, Shannon!

name = "Shannon"
greeting = "Hello, {0}".format(name)

print greeting

#writing the same thing as a function 

def greeting(name):
    name = "Shannon"
    print "Hello again,", name 
greeting("Shannon")
