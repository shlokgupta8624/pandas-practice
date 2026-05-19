import numpy as np
import pandas as pd
ipl =  r'C:\Users\Jai shree ram\OneDrive\Desktop\py.pd\deliveries.csv'
# ipl = pd.read_csv(ipl)
movies= pd.read_csv(r'C:\Users\Jai shree ram\OneDrive\Desktop\py.pd\imdb-top-1000 (1).csv')

print(movies.head())
genre = movies.groupby('Genre')
# how to get the highest rated movie from each genre? 
for group, data in genre:
    print(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])

# how many movies in each genre start with 'A'?     
def foo(group):
    return group['Series_Title'].str.startswith('A').sum()

genre.apply(foo)
# how to get the top 3 movies from each genre based on IMDB rating?
def rank(group):
    group['rank'] = group['IMDB_Rating'].rank(ascending=False)
    return group

genre.apply(rank)

# how to normalize the IMDB rating within each genre (min-max normalization)?
def formula(group):
  group['norm_rating'] = group['IMDB_Rating']-group['IMDB_Rating'].min()/ group['IMDB_Rating'].max()-group['IMDB_Rating'].min()
  return group

genre.apply(formula)

# how to calculate the average IMDB rating for each combination of Star1 and Genre?
movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False)

# how to find the top 10 batsmen with the most runs in the IPL?
ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

# # how to find top batsmen hitting most 4s and 6s in death overs? 
df = ipl[ipl['over'] > 15]
new_df = df[(df['batsman_runs'] == 4) | (df['batsman_runs'] == 6)]
result = new_df.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(10)
print(result)

# how to find the total runs scored by Virat Kohli against each bowling team in the IPL?
tem_df = ipl[ipl['batsman'] == 'V Kohli']
tem_df.groupby('bowling_team')['batsman_runs'].sum().reset_index()

# # how to rank movies within each genre based on rating? 
def rank(group):
    group['rank'] = group['IMDB_Rating'].rank(ascending=False)
    return group

genre.apply(rank)

# how to calculate the average IMDB rating for each combination of Star1 and Genre?
movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False)

# # how to find batsmen with most sixes? 
six = ipl[ipl['batsman_runs']== 6]
six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(10)

