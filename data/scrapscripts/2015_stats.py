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

    #rank count
    rank = 1

    #extract all player rows
    table_enteries = soup.findAll("tr", "pncPlayerRow")

    for tab in table_enteries:
        #create player dictionary to insert stats into
        player2015 = {}


        #extract the name of the player
        player2015["Name"] = tab.find("a", "flexpop").string

        #extract team name and position
        line = str(tab.find("td", "playertablePlayerName"))
        por = line[line.find("</a>")+6:-5]
        position = por[por.find("\xa0")+1:]
        if position == "D/ST":
            team = "--"
        else:
            team = por[:por.find("\xa0")-1]

        #Deal with injuries to players 
        if len(position) > 10:
            position = position[:position.find("\xc2")]

        

        #Get all season statistics
        stats = tab.findAll("td", "playertableStat")
        stats[0].split("/")[0]
        stats[0].split("/")[1]

