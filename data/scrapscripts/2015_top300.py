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
    names_elms = soup.find_all("a", "flexpop", )
    for elm in names_elms:
        val = elm.string
        if len(val.split(" ")) >= 3:
            #names.append(val)
            print(val)
    print(index)

print(names)
print(len(names))

#write csv file