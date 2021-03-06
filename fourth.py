#code showing how to read a file and title it
import pandas as pd
movies = pd.read_csv ('C:/Users/Modupe/Desktop/gitgirl/movies_metadata.csv', index_col = None)
named_movie = movies.set_index('title')
named_movie = movies.loc ['Grumpier Old Men']
print ('Data for movie titled - Grumpier Old Men:\n')
named_movie


#sort movies by their release dates
sortedmovies = movies.sort_values('release_date')
sortedmovies = sortedmovies.loc[:, ['title', 'release_date', 'budget', 'revenue', 'runtime']]
sortedmovies

#show movies which generated over 2 million with less than 1 million
revenue = sortedmovies[['revenue']] > 2000000
budget = sortedmovies[['budget']] < 1000000
sortedmovies[revenue & budget]
