import matplotlib.pyplot as plt
import pandas as pd

#Loading the dataset
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

#Merging the two Datasets
data = pd.merge(movies, ratings, on = 'movieId')

#Calculating average rating for each movie
movie_ratings = data.groupby('title')['rating'].mean().sort_values(ascending=False)

#Calculating the total number of rating for each movie
movie_rating_count = data.groupby('title')['rating'].count().sort_values(ascending=False)

#Creating a Datahrame with the average rating and the total umber of ratings for each movie
movie_stats = pd.DataFrame({'average_rating': movie_ratings, 'number_of_ratings':movie_rating_count})

#Plotting a histogram of the number of ratings
movie_stats['number_of_ratings'].hist(bins=50)

#Plotting a histogram of the average rating
movie_stats['average_rating'].hist(bins=50)

#Ploting a scatter plot of the average rating against the number of ratings
plt.scatter(movie_stats['average_rating'], movie_stats['number_of_ratings'])
plt.xlabel('Average Rating')
plt.ylabel('Number of Ratings')
plt.show()

#Printing the top 10 most popular movies
print(movie_stats.sort_values('number_of_ratings', ascending=False).head(10))

#Printing the top 10 best-rated movies
print(movie_stats.sort_values('average_rating', ascending=False).head(10))