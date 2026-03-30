import numpy as np
import pandas as pd

path = r'C:\Users\Jai shree ram\OneDrive\Desktop\py.pd\ipl-matches.csv'
newpath = r'C:\Users\Jai shree ram\OneDrive\Desktop\py.pd\movies.csv'

ipl = pd.read_csv(path)
movies= pd.read_csv(newpath)

# Creates a boolean mask where MatchNumber is 'Final'
mast = ipl['MatchNumber'] == 'Final'
new_df = ipl[mast]

# Selecting and printing only the Season and Winning Team for those finals
print("IPL Final Winners by Season:")
print(new_df[['Season', 'WinningTeam']])
print("-" * 30)

# 2. Count Super Overs
# .shape[0] counts the number of rows where a Super Over occurred
super_over_count = ipl[ipl['SuperOver'] == 'Y'].shape[0]
print(f"Total Super Overs in IPL history: {super_over_count}")

# 3. City-Specific Performance
# Filtering matches played in Kolkata
city_mask = ipl['City'] == 'Kolkata'
ndf = ipl[city_mask]

# Counting how many of those Kolkata matches were won by Chennai Super Kings
csk_kolkata_wins = ndf[ndf['WinningTeam'] == 'Chennai Super Kings'].shape[0]
print(f"CSK wins in Kolkata: {csk_kolkata_wins}")

# Calculating the percentage of matches where the Toss Winner also won the Match
toss_win_percent = (ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0] / ipl.shape[0]) * 100
print(f"Percentage of teams winning both Toss and Match: {toss_win_percent:.2f}%")
print("-" * 30)


# 5. High Engagement/Rating Filter
# Filtering movies with high ratings (or IDs) and a significant number of votes
# Note: Ensure 'imdb_id' shouldn't be 'imdb_rating' here for better accuracy
high_rated_count = movies[(movies['imdb_id'] > 8) & (movies['imdb_votes'] > 1000)].shape[0]
print(f"Number of highly rated/voted movies: {high_rated_count}")

# 6. Advanced Genre and Rating Filtering
# mask1: Splits the 'genres' string by '|' and checks if 'Action' is in the list
mask1 = movies['genres'].str.split('|').apply(lambda x : 'Action' in x)

# mask2: Filters for movies with an IMDb rating greater than 7.5
mask2 = movies['imdb_rating'] > 7.5

# Combining both masks to find High-Rated Action Movies
action_hits = movies[mask1 & mask2]

print("\nTop Rated Action Movies:")
print(action_hits[['movie_name', 'imdb_rating']].head()) # Showing top results

# Step 1: Count how many times each team appeared in the 'Team1' column
# Step 2: Count how many times each team appeared in the 'Team2' column
# Step 3: Add both counts together (Pandas aligns them by team name automatically)
# Step 4: Sort the results in descending order (highest matches first)

total_matches = (ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending=False)

print(total_matches)

ipl['TossDecision'].value_counts().plot(kind='pie')

# 1. isdigit() -> Finds numbers (1, 2, 3...) i.e. League Matches
# 2. ~ (Tilde) -> Means 'NOT'. So, it picks 'Final', 'Qualifier', etc.
# 3. value_counts() -> Counts who won 'Man of the Match' in these big games.

hero_stats = ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()

print(hero_stats)

# 1. 'split' breaks genres into a list; 'lambda' checks if 'Action' is in it
mask1 = movies['genres'].str.split('|').apply(lambda x : 'Action' in x)

# 2. Finds movies with an IMDb rating better than 7.5
mask2 = movies['imdb_rating'] > 7.5

# 3. '&' combines both: Only show Action movies with High Ratings
top_action = movies[mask1 & mask2]
# 4. Displaying the top-rated Action movies with their ratings

Action = movies[(movies['imdb_id'] > 8) & (movies['imdb_votes'] >1000)].shape[0]
print(f"Number of highly rated/voted movies: {Action}")
# Calculating the percentage of matches where the Toss Winner also won the Match
toss_win_percent = (ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100
print(f"Percentage of teams winning both Toss and Match: {toss_win_percent:.2f}%")
# Counting wins for a specific team in a specific city
city = ipl['City']== 'Kolkata'
ndf = ipl[city]
csk_wins_in_kolkata = ndf[ndf['WinningTeam'] == 'Chennai Super Kings'].shape[0]
print(f"CSK wins in Kolkata: {csk_wins_in_kolkata}")
