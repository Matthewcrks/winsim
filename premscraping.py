import requests
from bs4 import BeautifulSoup
import pandas as pd

#Extracting data happens in 3 steps
#1. load webpage containing the data
#2. locate the data within the page and extract it
#3. organize data into a dataframe


#LOAD WEBPAGE CONTAINING DATA


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

URL = "http://www.espn.com/soccer/stats/_/league/eng.1"
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


#locate the data and extract it

table = soup.find("table", {"class": "Table2__table-scroller Table2__table"}).tbody


nameVals = table.find_all("a")
goals = table.find_all("td", {"class": "tar Table2__td"})




print(goals[1].text)

playersList = []
teamsList = []
goalsList = []


for i in range (0,60):
	if i % 2 == 0:
		playersList.append(nameVals[i].text)
	else:
		teamsList.append(nameVals[i].text)
		goalsList.append(goals[i].text)

	i += 1

print('\n')

df = pd.DataFrame({"Players": playersList, "Team":teamsList, "Goals":goalsList})


print(df.head)

