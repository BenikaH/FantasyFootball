###Script to get ESPN 2015 projections for top 300 players
#base page: http://games.espn.go.com/ffl/tools/projections?display=alt
#next page: http://games.espn.go.com/ffl/tools/projections?display=alt&startIndex=15

#libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

#parameters
num_players = 300
index_increment = 15
start_index = 0
baseurl = "http://games.espn.go.com/ffl/tools/projections?display=alt&startIndex="

#set headers for csv
kicker_headers = ["1-39A", "1-39C", "40-49A", "40-49C", "50+A", "50+C", "TOTA", "TOTC", "XPA", "XPC"]
headers = ["Name", "Position", "Draft", "RUSH", "RUSHYDS", "RUSHAVG", "RUSHTD", "TAR", "REC", "RECYDS", "RECAVG", "RECTD", "C", "A", "COMPYDS", "COMPTD", "INT", "SCK", "DINT", "FR", "DTD", "PA", "YA"] + kicker_headers + ["PTS"]


allstats2014 = []
allproj2015 = []

#cycle through pages 
for index in range(start_index, num_players, index_increment):
    #Set the url and read in the raw html
    url = baseurl + str(index)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    
    #base player dictionary to add stats to
    player2014 = {}
    player2015 = {}
    for field in headers:
        player2014[field] = '--'
        player2015[field] = '--'

    #used to understand draft position as well as for debugging
    count = 1

    #find flex pop which describes the player name
    table_elms = soup.find_all("table", "tableBody")
    for tab in table_elms:
        #get player name
        player_name = tab.find("a","flexpop").string

        #get position and team initial
        brline = str(tab.find("nobr"))
        pos_end_loc = brline.find("</nobr>")
        pos_name = brline[pos_end_loc-2:pos_end_loc]
        team_name = brline[pos_end_loc-6:pos_end_loc-3]

        if pos_name == "ST":
            pos_name = "D/ST"
            team_name = "--"

        if pos_name == " K":
            pos_name = "K"
            team_name = brline[pos_end_loc-5:pos_end_loc-2]

        #get all stats
        allstats = tab.findAll("td", "playertableStat")
        statsres = []
        flag = True #meant for formatting of headers
        for stat in allstats:
            val = stat.contents[0].string

            #formatting so we do not have conflicting headers
            if (val == "YDS" or val == "TD"):
                if pos_name == "WR" or pos_name == "TE":
                    if flag:
                        val = "REC" + val
                        flag = False
                    else:
                        val = "RUSH" + val

                if pos_name == "QB":
                    if flag:
                        val = "COMP" + val
                        flag = False
                    else:
                        val = "RUSH" + val

                if pos_name == "RB":
                    if flag:
                        val = "RUSH" + val
                        flag = False
                    else:
                        val = "REC" + val

            if pos_name == "D/ST":
                if val == "INT" or val == "TD":
                    val = "D" + val

            if val == "AVG":
                if pos_name == "RB":
                    val = "RUSHAVG"
                else:
                    val = "RECAVG"

            if val.find("/") > 0:
                sp = val.split("/")
                statsres.append(sp[0])
                statsres.append(sp[1])
            elif val == "1-39" or val == "40-49" or val == "50+" or val == "TOT" or val == "XP":
                statsres.append(val+"C")
                statsres.append(val+"A")
            else:
                statsres.append(val)

        #get projected points
        allpts = tab.findAll("td", "playertableStat appliedPoints")
        pts2014 = allpts[1].string
        proj2015 = allpts[2].string

        #add stats to player dictionaries and put this in results
        player2014["Name"] = player2015["Name"] = player_name
        player2014["Position"] = player2015["Position"] = pos_name
        player2014["Draft"] = player2015["Draft"] = count + index

        size = len(statsres)/3
        for i in range(size):
            field = statsres[i]
            stat2014 = statsres[i+size]
            stat2015 = statsres[i+size+size]

            if stat2014.isdigit() or stat2014.find(".") > -1:
                player2014[field] = float(stat2014)
            else:
                player2014[field] = stat2014
            if stat2015.isdigit() or stat2015.find(".") > -1:
                player2015[field] = float(stat2015)
            else:
                player2015[field] = stat2015

        player2014["PTS"] = pts2014
        player2015["PTS"] = proj2015

        allstats2014.append(player2014.copy())
        allproj2015.append(player2015.copy())
        
        #increment count
        count += 1

    #put in place for progress purposes only        
    print("Index:" , index, "Count:", count)


#write csv file
with open('../raw_data/2015proj.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
    writer.writeheader()
    for piece in allproj2015:
        writer.writerow(piece)

with open('../raw_data/2014stats.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
    writer.writeheader()
    for piece in allstats2014:
        writer.writerow(piece)