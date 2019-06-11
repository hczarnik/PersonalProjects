import urllib.parse
import requests

apiLink = 'https://statsapi.web.nhl.com/api/v1/teams/'  #Website that gets information about the NHL teams
json_data = requests.get(apiLink).json()				#Return API data into JSON format so that it is readable and can be indexed
teamID = -1

userTeam = input("Enter team name: ")						#Take team from user
for x in range(31):
	team = json_data['teams'][x]['name']					#Put team name in variable	
	if userTeam.lower() in team.lower():					#Compare user's input to team
		teamID = json_data['teams'][x]['id']				#Store team ID from API into variable
		break

if teamID == -1:											#If the teamID variable is still -1, an invalid team was inputted.
	print('Invalid team')

teamLink = apiLink + str(teamID)							#Enter team ID to the link for the API
getRoster = teamLink + '?expand=team.roster'				#Appends modifier to link to get roster for team
json_data = requests.get(getRoster).json()					#Get JSON data for team roster website

LeftWings = []												#List for Left Wings
Centers = []												#List for Centers
RightWings = []											 	#List for Right Wings
Defensemen = []												#List for Defensemen
Goaltenders = []                                            #List for Goaltenders

for y in range(30):
	try:
		playerName = json_data['teams'][0]['roster']['roster'][y]['person']['fullName']
		playerPosition = json_data['teams'][0]['roster']['roster'][y]['position']['abbreviation']
		if playerPosition == 'LW':
			LeftWings.append(playerName)
		if playerPosition == 'C':
			Centers.append(playerName)
		if playerPosition == 'RW':
			RightWings.append(playerName)
		if playerPosition == 'D':
			Defensemen.append(playerName)
		if playerPosition == 'G':
			Goaltenders.append(playerName)
	except IndexError:
		break;

print(LeftWings)
print('\n')
print(Centers)
print('\n')
print(RightWings)
print('\n')
print(Defensemen)
print('\n')
print(Goaltenders)