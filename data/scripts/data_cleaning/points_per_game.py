import pandas as pd
import sys

if len(sys.argv) < 2:
    print ("add file name as first command line argument")
    raise("not enough args")

file_loc = sys.argv[1]

df  = pd.read_csv(file_loc, comment='#')

scoring_format = "FantPt"

if scoring_format not in df.columns:
    scoring_format = "FantPprPt"
    if scoring_format not in df.columns:
        raise("File does not have FantPt or FantPprpt as column header")

per_game = round(df.ix[:,scoring_format]/df.ix[:,"G"],2)

df[scoring_format+"pg"] = per_game

#/home/neeraj/Documents/Projects/FantasyFootball/data/actual_fantasy_pts_scored/ppr/ppr_fantasy_2016.csv
write_file = file_loc[:file_loc.rfind(".")-5] + "_per_game" + file_loc[file_loc.rfind(".")-5:]

print(df.to_csv(write_file))