## 1. Data Structures ##

import pandas as pd

fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head(2)

## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')

series_film = fandango["FILM"]
print(series_film.head(5))
series_rt = fandango["RottenTomatoes"]
print(series_rt.head(5))

## 3. Custom Indexes ##

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

series_custom = Series(index=film_names,data=rt_scores)

## 4. Integer Index Preservation ##

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

fiveten = series_custom[5:11]
print(fiveten)

## 5. Reindexing ##

original_index = series_custom.index
print(original_index[:10])
sorted_index = sorted(original_index)
print(sorted_index[:10])
sorted_by_index = series_custom.reindex(index=sorted_index)
print(sorted_by_index[:10])

## 6. Sorting ##

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2.head(10))
print(sc3.head(10))

## 7. Transforming Columns With Vectorized Operations ##

series_normalized = series_custom / 20

## 8. Comparing and Filtering ##

criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users) / 2