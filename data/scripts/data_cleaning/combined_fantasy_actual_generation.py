'''
Takes standard_fantasy_2014.csv  standard_fantasy_2015.csv  standard_fantasy_2016.csv and transforms them from standard scoring to ppr scoring
Takes full file name (starting from ~/...) as first command line argument
'''
import sys
import pandas as pd

if len(sys.argv) < 2:
    raise("add file name as first command line argument")

file_loc = sys.argv[1]
df =  pd.read_csv(file_loc)

df['FantPprPt'] = df["FantPt"].fillna(0) + df["Rec"].fillna(0)
df['FantPprPtpg'] = round((df["FantPt"].fillna(0) + df["Rec"].fillna(0))/df["G"],2)

output_file_name = "combined_" + file_loc.split("/")[-1]
df.to_csv(output_file_name)