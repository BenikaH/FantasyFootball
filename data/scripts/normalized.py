'''
Generates data to normalize data across all 16 games (even through injuries or missed games)

Inputs (sys.args):
    [1] actual_file - file location of fantasy performance for all players for a specific years
Outputs:
    csv file with normalized data for all players
'''
import sys
import pandas as pd
import numpy as np

if len(sys.argv) < 1:
    raise("No file specified")

actual_file_name = sys.argv[1]
df = pd.read_csv(actual_file_name)

multiplier = 16.0/df["G"]

# column names to normalize
column_names = ["Cmp","PassAtt","PassYds","PassTD","Int","RushAtt","RushYds","Y/A","RushTD","Tgt","Rec","RecYds","Y/R","RecTD","FantPt"]

#column names that have unaltered values that are indentifying and create dataframe
result_df = df[["Rk","Name","Tm","FantPos","Age","G","GS"]].copy()
for column_name in column_names:
    result_df[column_name] = df[column_name] if "/" in column_name else np.round(df[column_name]*multiplier,1)

#extra columns to add at the end. Not quite sure what some of these mean...
extra_columns = ["DKPt","FDPt","VBD","PosRank","OvRank","FantPtpg"]
for column_name in extra_columns:
    result_df[column_name] = df[column_name]

#export to a csv file
output_file_name = "normalized_" + actual_file_name.split("/")[-1]

result_df.to_csv(output_file_name, index=False)