'''
Takes names from data collection on profootball-reference and changes name to be of the format that is more friendly
Ex. Ezekiel Elliott*+\ElliEz00 -> Ezekiel Elliott
'''
import sys
import pandas as pd

if len(sys.argv) < 2:
    raise ("must have a file name! add file name as first command line argument")

file_loc = sys.argv[1]

df = pd.read_csv(file_loc)

names = df.ix[:,"Name"]
new_names = names.map(lambda x: x[:-9].replace("*","").replace("+",""))

df["Name"] = new_names

df.to_csv(file_loc)