##Neeraj Asthana
##Fantasy Football Predicion
##3/22/2016
###Script to get players birthdays and other related statistics for the 2015 NFL season
##base url for the data: "http://www.pro-football-reference.com/friv/birthdays.cgi?month=4&day=22"

#libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen
from datetime import date
import csv

baseurl = "http://www.pro-football-reference.com/friv/birthdays.cgi?month="

#September 10th 2015 was the first game
season_start = date(2015,9,10)

num_months = 12
num_days = 31

cutoff_year = 2015

players = []

for month in range(1,num_months+1):
    for day in range(1,num_days+1):

        #Set the url and read in the raw html
        url = baseurl + str(month) + "&day=" + str(day)
        print(url)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")

        #extract all player rows
        table_enteries = soup.findAll("tr")

        for i in range(2,len(table_enteries)):
            rows = table_enteries[i].findAll("td")

            #create player dictionary to insert stats into
            player2015 = {}

            #extract the name of the player
            player2015["Name"] = rows[1].string
            
            #positional and date information
            player2015["Position"] = rows[2].string
            player2015["Born"] = rows[3].string
            player2015["From"] = rows[4].string
            player2015["To"] = rows[5].string

            #other info
            player2015["AllProSelections"] = rows[6].string
            player2015["ProBowl"] = rows[7].string
            player2015["StartYears"] = rows[8].string
            player2015["GamesPlayed"] = rows[10].string

            if(player2015["To"] != "2015"):
                continue

            player2015["Month"] = month
            player2015["Day"] = day

            player2015["Age"] = (season_start - date(int(player2015["Born"]), month, day)).days

            players.append(player2015)


headers = ["Name", "Position", "Month", "Day", "Born", "From", "To", "AllProSelections", "ProBowl", "StartYears", "GamesPlayed", "Age"]

#write csv file

with open('../formatted_data/2015ages.csv', 'w') as csvfile:    
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for piece in players:
        writer.writerow(piece)