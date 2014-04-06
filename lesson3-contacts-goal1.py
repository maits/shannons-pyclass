# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
# Github: @shannonturner

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

contacts = {

'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturnet' },
'Anupama': {'phone': '410-333-9876', 'twitter': '@iamtheanupama', 'github': '@apillalamarri'},
'Maite': {'phone': '202-000-0000', 'twitter': '@maits', 'github': '@maits'},
'Lois': {'phone': '800-232-4500', 'twitter': '@lois', 'github': 'loisa'},
}

for contact,values in contacts.items():
	print "\n" "\t" "{0}'s contact information is:" "\n" "\t" .format(contact) + "Phone:" + ' ' + values.values()[0] + "\n" "\t"  "Twitter:" + ' ' + values.values()[1] + "\n" "\t"  "GitHub:" + ' ' + values.values()[2] 

