'''
Generates data for surrouding players for specific positions

Inputs (sys.args):
	[1] team_stats_file - file location of team statstics
	[2] actual_file - file location of fantasy performance for all players for a specific years
Outputs:
	csv file with postional data for surrounding players
'''

# Step 1 - read command line arguments and open csvs
import sys

team_stats_file = sys.argv[1]
actual_file = sys.argv[2]

team_stats = pd.read_csv(sys.argv[1])
actual = pd.read_csv(sys.argv[2])

# Step  - Match teams in team stats vs. actual player season stats