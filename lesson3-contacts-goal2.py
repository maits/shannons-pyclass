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

contacts = {

'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturnet' },
'Anupama': {'phone': '410-333-9876', 'twitter': '@iamtheanupama', 'github': '@apillalamarri'},
'Maite': {'phone': '202-000-0000', 'twitter': '@maits', 'github': '@maits'},
'Lois': {'phone': '800-232-4500', 'twitter': '@lois', 'github': 'loisa'},
}


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

#I'm sure there's an easier, better way of doing this but couldn't figure it out. Need to ask Shannon.
