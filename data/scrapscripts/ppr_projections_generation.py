'''
Takes 2015esponprojstats.csv and 2016esponprojstats.csv and transforms them from standard scoring to ppr scoring
Takes full file name (starting from ~/...) as first command line argument
'''
import csv
import sys

if len(sys.argv) < 2:
    print ("add file name as first command line argument")
else:
    file_loc = sys.argv[1]

    results = []

    with open(file_loc) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #Calculate ppr points value

            ppr_player_pts = 0
            if row['PTS'] == "--" and row['REC'] == "--":
                ppr_player_pts = 0
            elif row['PTS'] == "--":
                ppr_player_pts = round(float(row['REC']), 1)
            elif row['REC'] == "--":
                ppr_player_pts = round(float(row['PTS']), 1)
            else:
                ppr_player_pts = round(float(row['PTS']) + float(row['REC']), 1)

            new_player = row
            new_player['PPRPTS'] = ppr_player_pts
            new_player.pop('PTS')
            results.append(new_player)

    print(results[1].keys())

    #write file
    write_file = file_loc[:-4] + "ppr.csv"
    with open(write_file, 'w') as csvfile:
        fieldnames = results[1].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)
