#Exercise part 2:

#Loop through that dictionary to display everyone's contact information, like this:

#Shannon's contact information is:
#	Phone: 202-555-1234
#	Twitter: @svt827
#	Github: @shannonturner


contacts = {

'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturnet' },
'Anupama': {'phone': '410-333-9876', 'twitter': '@iamtheanupama', 'github': '@apillalamarri'},
'Maite': {'phone': '202-000-0000', 'twitter': '@maits', 'github': '@maits'},
'Lois': {'phone': '800-232-4500', 'twitter': '@lois', 'github': 'loisa'},
}

for contact,values in contacts.items():
		print "{0}'s contact information is:" "\n" "\t" .format(contact) + "Phone:" + ' ' + values.values()[0] + "\n" "\t"  "Twitter:" + ' ' + values.values()[1] + "\n" "\t"  "GitHub:" + ' ' + values.values()[2] 



