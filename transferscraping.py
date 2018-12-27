import requests
from bs4 import BeautifulSoup
import pandas as pd

#Extracting data happens in 3 steps
#1. load webpage containing the data
#2. locate the data within the page and extract it
#3. organize data into a dataframe


#LOAD WEBPAGE CONTAINING DATA


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

URL = "https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id=2000"
urlTree = requests.get(URL, headers=headers)
soup = BeautifulSoup(urlTree.content, 'html.parser')



#locate data within a page and extract it

players = soup.find_all("a", {"class": "spielprofil_tooltip"})


#print out first name in players list
print(players[0].text)


values = soup.find_all("td", {"class": "rechts hauptlink"})

print(values[0].text)


#organize into a dataframe

playersList = []
valuesList = []

for i in range(0,25):
	playersList.append(players[i].text)
	valuesList.append(values[i].text)


df = pd.DataFrame({"Players": playersList, "Values":valuesList})

print(df.head)