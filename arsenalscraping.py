#AUTHOR: MATTHEW CROOKS
#DATE: 12/27/18
#PURPOSE: I will scrape 538's data to find the win percentage of every single game that
# arsenal plays for the rest of the season. One more idea is using this data and comparing it 
# to their rivals to see how likely they are to win the title that season (take into account the current point deficit)
# eventual goal is to take a user input for the team whose win percentage they want to see
# ^ after that could add an option to specify a possible opponent and only see the percentages for that game

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

URL = "https://projects.fivethirtyeight.com/soccer-predictions/premier-league/"
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


#FOR FUTURE, ADD IN USER INPUT OPTION



#LOCATE AND EXTRACT DATA
overall=soup.find("div", {"class": "games-container upcoming"})



#right now i scrape the arsenal tag and get that fine but i'm struggling because the prob
# IS NOT listed under that arsenal tag

#couple of ways around this
#1. scrape every single team then make it a condition that if that a td has data-str then the next
# td will have the prob for that game so just read the next td using find

allBottom=overall.find_all("tr", {'class':'match-bottom'})
print(allBottom[6].text)


if "Arsenal" in allBottom[6].text:
	print("HELLO")

winProb = []

i = 0
while i < 30:
	if "Arsenal" in allBottom[i].text:
		print('imm here')
		winProb.append(allBottom[i].find("td", {'class':'prob'}).text)
	i += 1

for i in range(len(winProb)):
	print(winProb[i])
	i += 1
# this array has all of the win probabilities for arsenals away games




