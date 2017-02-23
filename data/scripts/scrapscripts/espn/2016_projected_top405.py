##Neeraj Asthana
##Fantasy Football Predicion
##3/22/2016
###Script to get ESPN 2016 stats for top 405 players

#libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

#parameters
num_players = 405
index_increment = 40
start_index = 0
baseurl = "http://games.espn.go.com/ffl/tools/projections?&seasonTotals=true&seasonId=2016&startIndex="

headers = ["Name", "Position", "Rank", "Team", "RUSH", "RUSHYDS", "RUSHTD", "REC", "RECYDS", "RECTD", "C", "A", "PASSYDS", "PASSTD", "INT", "PTS"]

#data structure to hold all of the players that we have parsed
players = []
rank = 1 #keep track of how well player did

for index in range(start_index, num_players, index_increment):
    #Set the url and read in the raw html
    url = baseurl + str(index)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    #extract all player rows
    table_enteries = soup.findAll("tr", "pncPlayerRow")

    for tab in table_enteries:
        #create player dictionary to insert stats into
        player2016 = {}


        #extract the name of the player
        player2016["Name"] = tab.find("a", "flexpop").string

        #extract team name and position
        line = str(tab.find("td", "playertablePlayerName"))
        por = line[line.find("</a>")+6:-5]
        position = por[por.find("\xa0")+1:]
        
        if position.find("<span") >= 0:
            position = position[:position.find("<span")-2]
        elif position.find("<a") >= 0:
            position = position[:position.find("<a")]

        if position == "D/ST":
            team = "--"
        else:
            team = por[:por.find("\xa0")]

        player2016["Position"] = position
        player2016["Team"] = team.replace(" ", "")

        #Get all season statistics
        stats = tab.findAll("td", "playertableStat")

        player2016["C"] = stats[0].string.split("/")[0]
        player2016["A"] = stats[0].string.split("/")[1]
        player2016["PASSYDS"] = stats[1].string
        player2016["PASSTD"] = stats[2].string
        player2016["INT"] = stats[3].string
        player2016["RUSH"] = stats[4].string
        player2016["RUSHYDS"] = stats[5].string
        player2016["RUSHTD"] = stats[6].string
        player2016["REC"] = stats[7].string
        player2016["RECYDS"] = stats[8].string
        player2016["RECTD"] = stats[9].string

        #add points and rank
        player2016["PTS"] = tab.find("td", "playertableStat appliedPoints").string
        player2016["Rank"] = rank
        rank += 1

        players.append(player2016)

        #progress of script
        print(rank)


#write csv file
with open('../formatted_data/2016espnprojstats.csv', 'w') as csvfile:    
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writeheader()
    for piece in players:
        writer.writerow(piece)