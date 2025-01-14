import pandas as pd#Imports the pandas library, which is used for data manipulation and analysis, especially for handling structured data like CSV files.
import matplotlib.pyplot as plt # Imports the pyplot module from matplotlib, which provides a MATLAB-like interface for making plots.
import seaborn as sns #Imports the seaborn library, which is built on top of matplotlib and provides a high-level interface for drawing attractive statistical graphics.

# Load the datasets
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# 1. Count the total number of matches conducted in the year 2008
matches_2008 = matches[matches['season'] == 2008]
total_matches_2008 = matches_2008.shape[0]
print(f'Total matches in 2008: {total_matches_2008}')

# 2. Find the city name where maximum and minimum number of matches conducted
city_counts = matches['city'].value_counts()
max_city = city_counts.idxmax()
min_city = city_counts.idxmin()
print(f'Max matches in: {max_city}, Min matches in: {min_city}')

# 3. Find total count of matches city-wise
print(city_counts)

# 4. Find the team which is maximum and minimum toss winner
toss_winners = matches['toss_winner'].value_counts()
max_toss_winner = toss_winners.idxmax()
min_toss_winner = toss_winners.idxmin()
print(f'Max toss winner: {max_toss_winner}, Min toss winner: {min_toss_winner}')

# 5. Check the toss decision that the team has taken
toss_decision_counts = matches['toss_decision'].value_counts()
print(toss_decision_counts)

# 6. Count the total number of normal and tie matches
normal_matches = matches[matches['result'] == 'normal'].shape[0]
tie_matches = matches[matches['result'] == 'tie'].shape[0]
print(f'Normal matches: {normal_matches}, Tie matches: {tie_matches}')

# 7. Find the team names where the match result is tie
tie_teams = matches[matches['result'] == 'tie'][['team1', 'team2']]# Filters the matches for those with a tie result and selects the columns for teams.
print(tie_teams)

# 8. Find the team name who won the match by highest runs
highest_win = matches.loc[matches['win_by_runs'].idxmax(), 'winner']
print(f'Team won by highest runs: {highest_win}')

# 9. Find the team name who won the match by lowest runs
lowest_win = matches.loc[matches['win_by_runs'].idxmin(), 'winner']
print(f'Team won by lowest runs: {lowest_win}')

# 10. Find the players who were awarded "Player of the Match" more than 3 times
potm_counts = matches['player_of_match'].value_counts()# Counts the number of times each player has been awarded "Player of the Match".
players_more_than_3 = potm_counts[potm_counts > 3]# Filters to find players awarded more than 3 times.
print(players_more_than_3)

# 11. Find the player who was awarded as player of the match maximum times
max_potm_player = potm_counts.idxmax()# Identifies the player with the maximum "Player of the Match" awards.
print(f'Player with maximum POTM awards: {max_potm_player}')

# 12. Find the venue where the team won the match by highest runs
venue_highest_run = matches.loc[matches['win_by_runs'].idxmax(), 'venue']
print(f'Venue with highest run win: {venue_highest_run}')

# 13. Find the venue where the team won the match by lowest runs
venue_lowest_run = matches.loc[matches['win_by_runs'].idxmin(), 'venue']
print(f'Venue with lowest run win: {venue_lowest_run}')

# 14. Find the umpires who officiated maximum times
umpires = pd.concat([matches['umpire1'], matches['umpire2']]).value_counts()# Combines both umpire columns into a single Series and counts occurrences.
max_umpires = umpires.idxmax()
print(f'Umpire who officiated maximum matches: {max_umpires}')

# 15. Find the total matches played in each season
season_counts = matches['season'].value_counts()
print(season_counts)

# 16. Find the total runs in each season
merged_data = deliveries.merge(matches[['id', 'season']], left_on='match_id', right_on='id')# This line merges two DataFrames: deliveries and a filtered version of matches that only includes the columns id and season.
total_runs = merged_data.groupby('season')['total_runs'].sum()#  For each group (each season), it sums the values in the total_runs column. This gives the total runs scored in each season across all matches.
print(total_runs)

# 17. No. of tosses won by each team
toss_wins = matches['toss_winner'].value_counts()
print(toss_wins)

# 18. Visualize the Toss decision across seasons
plt.figure(figsize=(10, 6))  # Specify figure size 10 inches wide and 6 inches tall
sns.countplot(data=matches, x='season', hue='toss_decision')
plt.title('Toss Decision across Seasons')
plt.xlabel('Seasons')
plt.ylabel('Count')
plt.legend(title='Toss Decision')
plt.show()  # Display the plot interactively

# 19. Find the Dismissal Kind and Visualize using a bar graph
plt.figure(figsize=(10, 6))  # Specify figure size
sns.countplot(data=deliveries, x='dismissal_kind')
plt.title('Dismissal Kind Distribution')
plt.xlabel('Dismissal Kind')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x labels for better visibility
plt.show()  # Display the plot interactively

# 20. Find the Top 10 run scorers in IPL and visualize
top_run_scorers = deliveries.groupby('batsman')['total_runs'].sum().nlargest(10)
plt.figure(figsize=(10, 6))  # Specify figure size
sns.barplot(x=top_run_scorers.index, y=top_run_scorers.values)
plt.title('Top 10 Run Scorers in IPL')
plt.xlabel('Batsman')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.show()  # Display the plot interactively

# 21. Visualize the Highest MOM award winners
highest_mom = potm_counts.nlargest(10)
plt.figure(figsize=(10, 6))  # Specify figure size
sns.barplot(x=highest_mom.index, y=highest_mom.values)
plt.title('Top MOM Award Winners')
plt.xlabel('Player')
plt.ylabel('Awards')
plt.xticks(rotation=45)
plt.show()  # Display the plot interactively

# 22. Find Total Number of Played Matches by each team
matches_played = matches['team1'].value_counts() + matches['team2'].value_counts()
print(matches_played)

# 23. Compare Total Played Matches vs Winning Matches vs Win Rate
win_counts = matches['winner'].value_counts()
win_rate = (win_counts / matches_played) * 100
comparison_df = pd.DataFrame({# A new DataFrame called comparison_df is created to consolidate the data. This DataFrame contains three columns:
    'Played Matches': matches_played,
    'Winning Matches': win_counts,
    'Win Rate (%)': win_rate
}).fillna(0)# any NaN values (for teams that might not have any wins or matches played) are replaced with 0. This is important for ensuring that all teams are represented in the DataFrame.
print(comparison_df)

# 24. Find the Distribution of Won Matches
sns.histplot(matches['winner'].value_counts(), bins=10)
plt.title('Distribution of Won Matches')
plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.show()  # Display the plot interactively

# 25. Ratio between Total Matches and Win Matches
win_ratios = matches_played / win_counts
print(win_ratios)

# 26. What is the choice of each team after winning the toss?
after_toss_choices = matches.groupby('toss_winner')['toss_decision'].value_counts()
print(after_toss_choices)

