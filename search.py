#AUTHOR: MATTHEW CROOKS
#DATE: 1/1/18
#PURPOSE:
# - to create a program that searches for a specific opponent for an arsenal given
# two magic number defined parameters: home or away and opponent


import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

URL = "https://projects.fivethirtyeight.com/soccer-predictions/premier-league/"
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


#LOCATE AND EXTRACT DATA
overall=soup.find("div", {"class": "games-container upcoming"})
stats = soup.find("table", {"class": "forecast-table"})
table = stats.find_all("tr", {'class':'team-row'})

#define winprob array
#winProb = []


allTop=overall.find_all("tr", {'class':'match-top'})
#divide up all the possible data that can be extracted from match top
#print(allTop[0].find("td", {'class':'date'}).text)
#print(allTop[0].find("td", {'class':'team'}).text)
#print(allTop[0].find("td", {'class':'prob'}).text)
#print(allTop[0].find("td", {'class':'prob tie-prob'}).text)


allBottom=overall.find_all("tr", {'class':'match-bottom'})
#print(allBottom[1].find("td", {'class':'team'}).text)
#print(allBottom[1].find("td", {'class':'prob'}).text)



team = input("\n(NOTE 1: Please use correct punctuation when specifying the team ie. Crystal Palace )\n(NOTE 2: For the Manchester clubs, enter Man. instead of Manchester. ie. Man. City)\n\nEnter the name of a team: ")
choice = input("\nWould you like to see (Press 1,2,or 3):\n1) " + team + "'s chance of making the top four and winning the title.\n2) " + team + "'s win probability for each of their remaining fixtures.\n3) " + team + "'s win probability vs. a certain opponent.\nOption: " )



if choice in '1':
	
	for m in range(len(table)):
		
		if team in table[m].text:
			specificteam = table[m].find_all("td", {"class":"pct"})
			ucl = specificteam[1].text
			title = specificteam[2].text
			print("\nChance of making UCL: " + ucl + "\nChances of winning title: " + title)



elif choice in '2':
	#find all the win probs for all remaining fixtures
	print("\nFormat: Date Team1 Team1WinProb (H) vs. Team2 Team2WinProb (A)")
	for i in range(len(allTop)):
		#check if home fixture
		if team in allTop[i].text:
			topProb = allTop[i].find("td", {'class':'prob'}).text
			opponent = allBottom[i].find("td", {'class':'team'}).text
			opponentProb = allBottom[i].find("td", {'class':'prob'}).text
			date = allTop[i].find("td", {'class':'date'}).text
			homeFix = date + " " + team + " " + topProb + " (H) vs. " + opponent + " " + opponentProb + " (A)"
			print(homeFix)

		if team in allBottom[i].text:
			awayProb = allBottom[i].find("td", {'class':'prob'}).text
			opponent = allTop[i].find("td", {'class':'team'}).text
			opponentProb = allTop[i].find("td", {'class':'prob'}).text
			date = allTop[i].find("td", {'class':'date'}).text
			print(date + " " + opponent + " " + opponentProb + " (H) vs. " + team + " " + awayProb + " (A)")




else:
	#print their schedule at this point just so they have a reference
	print("\n\nHere is " + team + "'s remaining schedule:")
	for i in range(len(allTop)):
		#check if home fixture
		if team in allTop[i].text:
			topProb = allTop[i].find("td", {'class':'prob'}).text
			opponent = allBottom[i].find("td", {'class':'team'}).text
			opponentProb = allBottom[i].find("td", {'class':'prob'}).text
			date = allTop[i].find("td", {'class':'date'}).text
			homeFix = date + " " + team + " (H) vs. " + opponent + " (A)"
			print(homeFix)
			
		if team in allBottom[i].text:
			awayProb = allBottom[i].find("td", {'class':'prob'}).text
			opponent = allTop[i].find("td", {'class':'team'}).text
			opponentProb = allTop[i].find("td", {'class':'prob'}).text
			date = allTop[i].find("td", {'class':'date'}).text
			print(date + " " + opponent + " (H) vs. " + team + " (A)")

	

	searchOpponent = input("\n\nEnter the name of an opponent: ")
	homeOrAway = input("Is " + team + " 'Home' or 'Away'?: ")


	if 'Home' in homeOrAway:

		for i in range(len(allTop)):

			if team in allTop[i].text and searchOpponent in allBottom[i].text:

				topProb = allTop[i].find("td", {'class':'prob'}).text
				opponent = allBottom[i].find("td", {'class':'team'}).text
				print(team + "'s win probability in their home fixture vs. " + searchOpponent + " is: " + topProb)

	else:

		for i in range(len(allBottom)):

			if team in allBottom[i].text and searchOpponent in allTop[i].text:

				teamProb = allBottom[i].find("td", {'class':'prob'}).text
				opponent = allTop[i].find("td", {'class':'team'}).text
				print(team + "'s win probability in their away fixture vs. " + searchOpponent + " is: " + teamProb)





