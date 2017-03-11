import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#projs = pd.read_csv("../../data/projections_espn/2016espnprojstats.csv")
#actual = pd.read_csv("../../data/actual_fantasy_pts_scored/standard/standard_fantasy_2016.csv")

if len(sys.argv) < 3:
    raise("Not enough args in input. Should include projections file first, then actual points scored file, and then optional position")
projs = pd.read_csv(sys.argv[1])
actual = pd.read_csv(sys.argv[2])

projs = projs.ix[:,["Name","PTS"]]

# Get displaying position. If none is specified, just displays all positions
positions = ["QB", "WR", "RB", "TE"]
position = "ALL"
if len(sys.argv) > 3:
    if sys.argv[3] in positions:
        position = sys.argv[3]

def change_na(x, divide=16.0):
    if x == "--":
        return 0
    return float(x)/divide

projs["PTSPG"] = projs.ix[:,"PTS"].apply(lambda x: change_na(x))
projs["PTS"] = projs.ix[:,"PTS"].apply(lambda x: change_na(x,divide=1.0))
actual = actual.ix[:,["Name","G","FantPt","FantPtpg","FantPos"]]

#merge arrays and reset index
df = pd.merge(projs, actual, on="Name")
df = df[df.FantPos == position].reset_index()
del df["index"]

def position_to_color(player):
    if position is "ALL":
        pos = player["FantPos"]
        if pos == "QB":
            return 1
        elif pos == "WR":
            return 2
        elif pos == "RB":
            return 3
        elif pos == "TE":
            return 4
        else:
            return 5
    else:
        if player["FantPtpg"] > player["PTSPG"]:
            return 1,"Above"
        else:
            return 2,"Below"


colors_and_labels = np.array([position_to_color(player) for index,player in df.iterrows()])

x = df['PTSPG']
y = df['FantPtpg']

fig = plt.figure()
ax = fig.add_subplot(111)

plt.scatter(x,y, c = colors_and_labels[:,0])
plt.xticks(np.arange(min(x), max(x)+1, 2))
plt.yticks(np.arange(0, max(y)+1, 2))
plt.grid(linestyle='--')

for i,xy in enumerate(zip(x, y)):
    player_name = df.ix[i,"Name"]
    name = player_name[0] + ". " + player_name.split(" ")[-1] + " - " + str(df.ix[i,"G"])
    ax.annotate(name, xy=xy, textcoords='data')

# now plot both limits against eachother
plt.plot(np.arange(min(max(x)+1,max(y))), 'r--', label='Random guess')

#Title and axis labels
year = sys.argv[1].split("/")[-1][:4]
plt.title(year + " Actual PPG Scored vs. ESPN Expected PPG - " + position)
plt.ylabel("Actual PPG Scored")
plt.xlabel("ESPN Expected PPG")


plt.show()