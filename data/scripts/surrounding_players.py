'''
Generates data for surrouding players for specific positions

Inputs (sys.args):
    [1] team_stats_file - file location of team statstics
    [2] actual_file - file location of fantasy performance for all players for a specific years
Outputs:
    csv file with postional data for surrounding players
'''
import sys
import pandas as pd

# Step 1 - read command line arguments and open csvs and clean data

team_stats_file = sys.argv[1]
actual_file = sys.argv[2]

team_stats = pd.read_csv(sys.argv[1])
actual = pd.read_csv(sys.argv[2])

if 'G' in list(team_stats):
    del team_stats['G']

# Step 2 - Match teams in team stats vs. actual player season stats.
#          Change team statistics column for "Tm" to actual player dataset's representation
team_dictionary = {
    "Atlanta Falcons": "ATL",
    "New Orleans Saints": "NOR",
    "New England Patriots": "NWE",
    "Green Bay Packers": "GNB",
    "Dallas Cowboys": "DAL",
    "Arizona Cardinals": "ARI",
    "Oakland Raiders": "OAK",
    "Indianapolis Colts": "IND",
    "San Diego Chargers": "SDG",
    "Pittsburgh Steelers": "PIT",
    "Buffalo Bills": "BUF",
    "Washington Redskins": "WAS",
    "Kansas City Chiefs": "KAN",
    "Tennessee Titans": "TEN",
    "Carolina Panthers": "CAR",
    "Philadelphia Eagles": "PHI",
    "Miami Dolphins": "MIA",
    "Seattle Seahawks": "SEA",
    "Tampa Bay Buccaneers": "TAM",
    "Detroit Lions": "DET",
    "Baltimore Ravens": "BAL",
    "Denver Broncos": "DEN",
    "Minnesota Vikings": "MIN",
    "Cincinnati Bengals": "CIN",
    "Jacksonville Jaguars": "JAX",
    "New York Giants": "NYG",
    "San Francisco 49ers": "SFO",
    "Chicago Bears": "CHI",
    "Houston Texans": "HOU",
    "New York Jets": "NYJ",
    "Cleveland Browns": "CLE",
    "Los Angeles Rams": "LAR"
}

for index, row in team_stats.iterrows():
    team_stats.ix[index,"Tm"] = team_dictionary[row["Tm"]]


# Step 3 - Match players with team stats
df = pd.merge(actual, team_stats,on="Tm", suffixes=["","Tm"])

# Step 4 - Add columns with player stats subtracted from team totals (accurate team contribution)