import json
import requests
fpl_data = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static').json()
for i, player in enumerate(fpl_data['elements']):
	fpl_data['elements'][i]['history'] = requests.get('https://fantasy.premierleague.com/drf/element-summary/' + str(player['id'])).json()

open('fpldata.txt', 'w').close()
with open('fpldata.txt', 'w') as outfile:
	json.dump(fpl_data, outfile)



