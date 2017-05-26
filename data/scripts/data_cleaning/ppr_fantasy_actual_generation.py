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
"""
df.drop('reports', axis=1)

    with open(file_loc) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #Calculate ppr points value

            ppr_player_pts = 0
            if row['FantPt'] == "" and row['Rec'] == "":
                ppr_player_pts = 0
            elif row['FantPt'] == "":
                ppr_player_pts = round(float(row['Rec']), 1)
            elif row['Rec'] == "":
                ppr_player_pts = round(float(row['FantPt']), 1)
            else:
                ppr_player_pts = round(float(row['FantPt']) + float(row['Rec']), 1)

            new_player = row
            new_player['FantPprPt'] = ppr_player_pts
            new_player.pop('FantPt')
            results.append(new_player)

    print(results[1].keys())

    #write file
    write_file = "ppr" + file_loc[file_loc.rfind("/")+9:]
    with open(write_file, 'w') as csvfile:
        fieldnames = results[1].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)
"""