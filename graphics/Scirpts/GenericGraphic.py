import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#Parse command line args 
if len(sys.argv) < 5:
    raise("Not enough args in input. Should include projections file first, then actual points scored file, and 2 columns to graph against, and then optional position")
projs_file = sys.argv[1]
actual_file = sys.argv[2]
projs_column = sys.argv[3]
actual_column = sys.argv[4]
positions = ["QB", "WR", "RB", "TE"]
position = "ALL"
if len(sys.argv) > 5 :
    if sys.argv[5] in positions:
        position = sys.argv[5]

#Read csv files
projs = pd.read_csv(sys.argv[1])
actual = pd.read_csv(sys.argv[2])

#Removing repeated name (David Johnson) if neccessary 
#djname = actual["Name"] != "David Johnson"
#djposnotTE = actual["FantPos"] != "TE"
#actual = actual[[x or y for x, y in zip(djname, djposnotTE)]]

#Reduce csvs down to simple columns I need (specified in command line)
projs = projs.ix[:,["Name",projs_column]]
actual = actual.ix[:,["Name",actual_column, "FantPos"]]

#Data Cleaning (deal with missing/NA values) -> "--" represents a missing value
def change_na(x, divide=1.0):
    if x == "--":
        return 0
    return float(x)/divide

projs[projs_column] = projs.ix[:,"PTS"].apply(lambda x: change_na(x))

#merge arrays and reset index
df = pd.merge(projs, actual, on="Name")
if position is not "ALL":
    df = df[df.FantPos == position]
df = df.reset_index()
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
        return 1


colors_and_labels = np.array([position_to_color(player) for index,player in df.iterrows()])

x = df[projs_column]
y = df[actual_column]

fig = plt.figure()
ax = fig.add_subplot(111)

if position is "ALL":
    plt.scatter(x,y, c = colors_and_labels)
else:
    plt.scatter(x,y)

tick_range = max(int( (max(x) - min(x))/10), int((max(y) - min(y))/10))
plt.xticks(np.arange(min(x)-1, max(x)+1, tick_range))
plt.yticks(np.arange(min(y)-1, max(y)+1, tick_range))
plt.grid(linestyle='--')

for i,xy in enumerate(zip(x, y)):
    player_name = df.ix[i,"Name"]
    name = player_name[0] + ". " + player_name.split(" ")[-1] #+ " - " + str(df.ix[i,"G"])
    ax.annotate(name, xy=xy, textcoords='data')

# now plot both limits against eachother
plt.plot(np.arange(min(max(x)+1,max(y))), 'r--', label='Random guess')

#Title and axis labels
year = projs_file.split("/")[-1][:4]
plt.title(year + " " + actual_column + " vs " + projs_column + " - "+ position)
plt.ylabel(actual_column)
plt.xlabel(projs_column)


plt.show()