"""
Uses surrounding player data to do pca to find best features for QB
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import sys
import matplotlib.pyplot as plt

# Options include either 2014, 2015, 2016
year = sys.argv[1]
size = sys.argv[2]
file_name = "../../data/surrounding_players/surrounding_players_" + year + ".csv"
 
#read file into data frame and reduce to just QB
df = pd.read_csv(file_name)
df = df[df.FantPos == "QB"]
df = df.sort_values("FantPtpg", ascending=False).head(int(size))



fantPt = df["FantPt"]
fantPtpg = df["FantPtpg"]
name = df["Name"]

#Rk,Name,Tm,FantPos,Age,G,GS,Cmp,PassAtt,PassYds,PassTD,Int,RushAtt,RushYds,Y/A,RushTD,Tgt,Rec,RecYds,Y/R,RecTD,FantPt,DKPt,FDPt,VBD,PosRank,OvRank,FantPtpg,RkTm,PF,TotalYds,Ply,Y/P,TO,FL,Pass1stD,CmpTm,PassAttTm,PassYdsTm,PassTDTm,IntTm,NY/A,Pass1stD.1,RushAttTm,RushYdsTm,RushTDTm,Y/ATm,Rush1stD,Pen,PenYds,1stPy,Sc%,TO%,EXP,RushTDTmSans,RushAttTmSans,RushYdsTmSans,CmpTmSans,PassAttTmSans,PassYdsTmSans,PassTDTmSans,IntTmSans,RecTmSans,TgtTmSans,RecYdsTmSans,RecTDTmSans
df = df.drop(["Rk", "Name", "Tm","FantPos","GS","PassYds","PassTD","Int","RushYds","Y/A","RushTD","Tgt","Rec","RecYds","Y/R","RecTD","FantPt","DKPt","FDPt","VBD","PosRank","OvRank","FantPtpg","RkTm","Pass1stD","CmpTm","PassAttTm","PassYdsTm","PassTDTm","IntTm","NY/A","Pass1stD.1"],axis=1)

df[['Cmp','PassAtt','RushAtt']].div(df.G, axis=0)


# PCA
pca = PCA(n_components=10)
pca.fit(df,fantPtpg)

# Plot Skree Plot
#print(pca.explained_variance_ratio_)
#plt.plot(pca.explained_variance_ratio_)
#plt.title(year + " Skree Plot for QB")
#plt.xlabel("component")
#plt.show()

#plot first 2 components
transformed_new = pca.fit_transform(df)

plt.scatter(np.array(transformed_new)[:,0],np.array(transformed_new)[:,1])
plt.title(year + " top " + str(size) + " QB 2 Component PCA")

for i in range(len(name)):
    player_name = name.iloc[i]
    player_name = player_name[0] + ". " + player_name.split(" ")[-1] + " - " + str(fantPtpg.iloc[i])
    plt.annotate(player_name, xy=(transformed_new[i,0],transformed_new[i,1]), textcoords='data')

plt.show()