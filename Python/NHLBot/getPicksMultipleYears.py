import urllib.parse
import requests

""" This program is an extension of getPicks.py. In this program, a user may request to see a list of draft picks
from the most recent draft to a year of their choosing. 

TODO:
(1) -Allow teamID to be changed so that all teams may be researched """

apiLink = 'https://statsapi.web.nhl.com/api/v1/draft/'	#Link to API
currentYear = 2018										#Most recent draft
teamID = 1												#Team ID, current ID links to the New Jersey Devils, check TODO (1)

years = input('Enter number of years to go back: ')		#Ask user how many years to go back to

print('New Jersey Devils draft picks from the previous ' + years + ' Entry Drafts:')
print()

for year in range(int(years)):					#For every year, the program will print out each draft pick for the team
	yearLink = apiLink + str(currentYear)		#Appends the current year to the API link
	json_data = requests.get(yearLink).json()	#Gets API data in JSON format
	print(str(currentYear) + ':')				#Prints year of draft that is looked at for user to see
	for roundNo in range(7):					#There are 7 rounds in the modern NHL drafts
		for eachPick in range(31):				#There are 31 teams in the current NHL format
			try:
				currentPick = json_data['drafts'][0]['rounds'][roundNo]['picks'][eachPick]['team']['id']	#Scans each pick and takes the team ID that made the pick
				if(currentPick == teamID):	#If the pick was made by the team being looked at in this program, print the round, overall pick, and player name information
					roundPickNumber = json_data['drafts'][0]['rounds'][roundNo]['picks'][eachPick]['pickInRound']
					overallPickNumber = json_data['drafts'][0]['rounds'][roundNo]['picks'][eachPick]['pickOverall']
					player = json_data['drafts'][0]['rounds'][roundNo]['picks'][eachPick]['prospect']['fullName']
					print('Round ' + str(roundNo+1) + ' pick ' +str(roundPickNumber)+ ' ('+ str(overallPickNumber)+ ' overall): ' + player)
			except IndexError:	#If a year is chosen where there are less than 31 teams, this exception prevents an IndexError and continues with the loop
				break;
	currentYear -= 1