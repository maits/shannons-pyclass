contacts = {

'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturnet' },
'Anupama': {'phone': '410-333-9876', 'twitter': '@iamtheanupama', 'github': '@apillalamarri'},
'Maite': {'phone': '202-000-0000', 'twitter': '@maits', 'github': '@maits'},
'Lois': {'phone': '800-232-4500', 'twitter': '@lois', 'github': 'loisa'},
}



for contact in contacts.keys():
	print contact

for contact in sorted(contacts.keys()):
	print contact

for info in contacts.values():
	print info

for contact, info in contacts.items():
  print contact, info
