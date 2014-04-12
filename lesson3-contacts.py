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

# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

for contact,values in contacts.items():
		print "\n"
		print '<table border="1">'
		print '<tr>'
		print '<td colspan="2">'  
		print contact
		print '</td>' 
		print '</tr>' 
		print '<tr>' 
		print '<td>'"Phone:" + ' ' + values.values()[0] 
		print '</td>'
		print '<td>'"Twitter:" + ' ' + values.values()[1] 
		print '</td>' 
		print '<td>'"GitHub:" + ' ' + values.values()[2]
		print '</td>' 
		print '</tr>'
		print '</table>'

#I found a better way of doing this in ElizabethAB's github

html_string = ""

for contact, info in contacts.items():
	html_string += """<table border="1">
<tr>
<td colspan="2"> {0} </td>
</tr>
<tr>
<td> Phone: {1} </td>
<td> Twitter: {2} </td>
<td> Github: {3} </td>
</tr>
</table>
	""".format(contact, info.get('phone'), info.get('twitter'), info.get('github'))
	print html_string

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

with open('contacts.html','w') as newfile:
	newfile.write(html_string)

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).

file_contacts = {}

with open("contacts.csv",'r') as contacts_file: #I downloaded the CSV to my desktop. This assumes both files are in the desktop.
	contacts_string = contacts_file.read().split('\n')[1:]

for contact in contacts_string:
	contactlist = contact.split(',')
	file_contacts[contactlist[0]]={'phone' : contactlist[1], 'twitter' : contactlist[2], 'github' : contactlist[3]}

#this doesn't work. It gives me an Index Error - list index is out of range. 
