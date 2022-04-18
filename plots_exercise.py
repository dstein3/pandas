import pandas as pd

plots = pd.read_csv('wiki_movie_plots_deduped.csv')

#1
print(len(plots))

#2
print(plots.shape)

#3
print(plots.info())

#4
print(plots[len(plots)-8:])

#6
print(plots.tail(8))

#7
print(plots[1:5])

#8
print(plots.head())

#9
print(plots.columns)
print(plots.Genre.value_counts().head(5))

#10
print(plots.Director.value_counts().head(5))

#11
#print(plots.Origin/Ethnicity.value_counts())

#12
print(plots.Title.value_counts())

#13
print(plots.Release_Year.value_counts().head(1))