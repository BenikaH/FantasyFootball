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

#cycle through pages 
for i in range(startIndex, num_players, index_increment):
	#Set the url and read in the raw html
	url = baseurl + str(i)
	html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    
    #find flex pop which describes the player name
    boccat = soup.find("dl", "flexpop")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links

#write csv file