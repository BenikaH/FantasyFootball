###Script to get ESPN 2015 projections for top 300 players
#base page: http://games.espn.go.com/ffl/tools/projections?display=alt
#next page: http://games.espn.go.com/ffl/tools/projections?display=alt&startIndex=15

#libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen

#parameters
num_players = 300
index_increment = 15
start_index = 0
baseurl = "http://games.espn.go.com/ffl/tools/projections?display=alt&startIndex="

names = []

#cycle through pages 
for index in range(start_index, num_players, index_increment):
    #Set the url and read in the raw html
    url = baseurl + str(index)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    
    #find flex pop which describes the player name
    table_elms = soup.find_all("table", "tableBody")
    for tab in names_elms:
        #get player name
        player_name = table_elms[0].find("a","flexpop").string

        #get position and team initial
        brline = str(table_elms[0].find("nobr"))
        pos_end_loc = brline.find("</nobr>")
        pos_name = brline[pos_end_loc-2,pos_end_loc]
        team_name = brline[pos_end_loc-6:pos_end_loc-3]

        #get all stats
        allstats = tab.findAll("td", "playertableStat")
        statsres = []
        for stat in allstats:
            val = stat.contents[0].string
            statsres.append(val)

        #get projected points
        allpts = tab.findAll("td", "playertableStat appliedPoints")
        pts2014 = allpts[1].string
        proj2015 = allpts[2].string

    #put in place for progress purposes only        
    print(index)

print(names)
print(len(names))

#write csv file