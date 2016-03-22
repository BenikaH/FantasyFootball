###Script to get ESPN 2015 stats for top 350 players
#http://games.espn.go.com/ffl/leaders?&startIndex=0

#libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

#parameters
num_players = 50
index_increment = 50
start_index = 0
baseurl = "http://games.espn.go.com/ffl/leaders?&startIndex="

headers = ["Name", "Position", "Rank", "RUSH", "RUSHYDS", "RUSHTD", "TAR", "REC", "RECYDS", "RECTD", "C", "A", "COMPYDS", "COMPTD", "INT"] + ["PTS", "TEAM"]

for index in range(start_index, num_players, index_increment):
    #Set the url and read in the raw html
    url = baseurl + str(index)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    #extract all player rows
    table_enteries = soup.findAll("tr", "pncPlayerRow")

    for tab in table_enteries:
        #extract the name of the player
        name = tab.find("a", "flexpop").string

        #extract team name and position
        line = str(tab.find("td", "playertablePlayerName"))
        por = line[line.find("</a>")+6:-5]
        position = por[por.find("\xa0")+1:]
        if position == "D/ST":
            team = "--"
        else:
            team = por[:por.find("\xa0")-1]

        print(name, team, position)
