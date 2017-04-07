'''
Removes all unamed columns that are either unlabeled or named "unnamed" from a pandas dataframe
'''
import sys
import pandas as pd

if len(sys.argv) < 1:
	raise("Not enough args in input. Should include file location first")
file_name = sys.argv[1]
file = pd.read_csv(file_name)

removal_col_names = []
for col in list(file):
	if "Unnamed" in col:
		removal_col_names.append(col)

for col_name in removal_col_names:
	del file[col_name]

file.to_csv(file_name, index=False)