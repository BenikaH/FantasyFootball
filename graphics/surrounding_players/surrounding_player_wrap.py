import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#Parse command line args 
if len(sys.argv) < 4:
    raise("Not enough args in input. Should include projections file first, then actual points scored file, and 2 columns to graph against, and then optional position")
file_name = sys.argv[1]
projs_column = sys.argv[2]
actual_column = sys.argv[3]
positions = ["QB", "WR", "RB", "TE"]
position = "ALL"
if len(sys.argv) > 4 :
    if sys.argv[4] in positions:
        position = sys.argv[4]

#Number of players to grab
size = 0
if len(sys.argv) > 5:
    size = sys.argv[5]

#Whether to display per game averages or not
per_game = False
if len(sys.argv) > 6 and sys.argv[6].lower() == "pg":
    per_game = True

#Read csv files
df = pd.read_csv(sys.argv[1])

#Limits size based on user passed in args
if len(sys.argv) < 5 or size.lower() == "all":
    size = len(df.index)

#Reduce csvs down to simple columns I need (specified in command line)
df = df.ix[:,["Name","G",projs_column,actual_column, "FantPos"]]

if position is not "ALL":
    df = df[df.FantPos == position]
df = df.reset_index()
del df["index"]
df.fillna(0)

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
        return 1


colors_and_labels = np.array([position_to_color(player) for index,player in df.iterrows()])

if len(sys.argv) > 5:
    if per_game:
        if "Sans" in actual_column:
            df[actual_column + "pg"] = df[actual_column]/16
        else: 
            df[actual_column + "pg"] = df[actual_column]/df["G"]
        actual_column = actual_column +"pg"
    df = df.sort_values(projs_column, ascending=False).head(int(size))

x = df[projs_column]
y = df[actual_column]


fig = plt.figure()
ax = fig.add_subplot(111)

if position is "ALL":
    plt.scatter(x,y, c = colors_and_labels)
else:
    plt.scatter(x,y)

plt.xticks(np.arange(min(x)-.5, max(x)+.5, round( (max(x) - min(x))/10)/2 ))
plt.yticks(np.arange(min(y)-1, max(y)+1, round( (max(y) - min(y))/10)/2) )
plt.grid(linestyle='--')

# annotate points with player names
for i,row in df.iterrows():
    player_name = row["Name"]
    name = player_name[0] + ". " + player_name.split(" ")[-1] #+ " - " + str(df.ix[i,"G"])
    ax.annotate(name, xy=(row[projs_column],row[actual_column]), textcoords='data')

#Title and axis labels
year = file_name.split("/")[-1].split(".")[0][-4:]
plt.title(year + " " + actual_column + " vs " + projs_column + " - "+ position)
plt.ylabel(actual_column)
plt.xlabel(projs_column)


plt.show()