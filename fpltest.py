import json

fpl_data = open('fpldata.txt').read()

data = json.loads(fpl_data)

for i in data['elements']:
	for j in i:
		if j == 'first_name':
			if i['first_name'] == 'Abel':
				print i['web_name']
				print "----------\n---------"
			if i['first_name'] == 'Alexis':
				print i['web_name']
				print "----------\n---------"
			if i['first_name'] == 'Kun':
				print i['web_name']
				print "----------\n---------"
			if i['first_name'] == 'Sadio':
				print i['web_name']
				print "----------\n---------"
			if i['first_name'] == 'Mesut':
				print i['web_name']
				print "----------\n---------"
			if i['first_name'] == 'Leroy':
				print i['web_name']
				print "----------\n---------"
			if i['first_name'] == 'Manuel':
				print i['web_name']
			if i['first_name'] == 'Pedro':
				print i['web_name']
				
			
