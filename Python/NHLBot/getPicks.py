import urllib.parse
import requests

apiLink = 'https://statsapi.web.nhl.com/api/v1/draft/2018'
json_data = requests.get(apiLink).json()
teamID = 1

print('New Jersey Devils draft picks from the 2018 Entry Draft:')
print()

for roundNo in range(7):
	for eachPick in range(31):
		currentPick = json_data['drafts'][0]['rounds'][roundNo]['picks'][eachPick]['team']['id']
		if(currentPick == teamID):
			player = json_data['drafts'][0]['rounds'][roundNo]['picks'][eachPick]['prospect']['fullName']
			print('Round ' + str(roundNo+1) + ' pick: ' + player)