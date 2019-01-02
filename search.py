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



team = input("Enter the name of a team: ")
searchOpponent = input("Enter the name of an opponent: ")
homeOrAway = input("'Home' or 'Away'? ")



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





