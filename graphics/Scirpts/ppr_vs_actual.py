"""
Uses combined.csv file as imput (has both ppr and standard scoring data)
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    raise("add file name as first command line argument")

positions = ["QB", "WR", "RB", "TE"]
position = "ALL"
if len(sys.argv) > 2 :
    if sys.argv[2] in positions:
        position = sys.argv[2]

file_loc = sys.argv[1]
df =  pd.read_csv(file_loc).ix[:300,:]

if position is not "ALL":
    df = df[df.FantPos == position]
df = df.reset_index()
del df["index"]

x = df["FantPtpg"]
y = df["FantPprPtpg"]
names = df["Name"]

# Compute all colors for datapoints
def position_to_color(player):
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
colors_and_labels = np.array([position_to_color(player) for index,player in df.iterrows()])

#Create plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(x,y, c = colors_and_labels)
plt.plot(range(1+int(min(max(x),max(y)))))
plt.grid(linestyle='--')

#Add names to plot
for i,xy in enumerate(zip(x, y)):
    player_name = df.ix[i,"Name"]
    name = player_name[0] + ". " + player_name.split(" ")[-1] #+ " - " + str(df.ix[i,"G"])
    ax.annotate(name, xy=xy, textcoords='data')

year = file_loc.split("/")[-1][-8:-4]
plt.title(year + " ppr scoring vs standard scoring")
plt.ylabel("PPR per game")
plt.xlabel("Standard per game")

plt.show()

plt.savefig('/home/neeraj/Documents/Projects/FantasyFootball/graphics/ppr_vs_standard/'+year+'_'+position+'_PPR_vs_Standard.png')