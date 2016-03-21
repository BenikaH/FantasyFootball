###Script to get ESPN 2015 stats for top 350 players
#http://games.espn.go.com/ffl/leaders?&startIndex=0

#libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

#parameters
num_players = 350
index_increment = 50
start_index = 0
baseurl = "http://games.espn.go.com/ffl/leaders?&startIndex="

headers = ["Name", "Position", "Rank", "RUSH", "RUSHYDS", "RUSHTD", "TAR", "REC", "RECYDS", "RECTD", "C", "A", "COMPYDS", "COMPTD", "INT"] + ["PTS", "TEAM"]

for index in range(start_index, num_players, index_increment):
	