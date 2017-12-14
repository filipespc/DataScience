## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(411,xlim=(0,5))
ax2 = fig.add_subplot(412,xlim=(0,5))
ax3 = fig.add_subplot(413,xlim=(0,5))
ax4 = fig.add_subplot(414,xlim=(0,5))

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

## 2. Mean ##

def calc_mean(series):
    return series.mean()

user_reviews = movie_reviews[["RT_user_norm","Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]].copy()
[rt_mean, mc_mean, fg_mean, id_mean] = user_reviews.apply(calc_mean)

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    variance = 0
    mean = calc_mean(series)
    for each in series:
        variance += (each - mean)**2
    variance = variance/len(series)
    return variance

rt_var = calc_variance(movie_reviews["RT_user_norm"])
rt_stdev = rt_var**(1/2)

mc_var = calc_variance(movie_reviews["Metacritic_user_nom"])
mc_stdev = mc_var**(1/2)

fg_var = calc_variance(movie_reviews["Fandango_Ratingvalue"])
fg_stdev = fg_var**(1/2)

id_var = calc_variance(movie_reviews["IMDB_norm"])
id_stdev = id_var**(1/2)

## 4. Scatter plots ##

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(311,xlim=(0,5))
ax2 = fig.add_subplot(312,xlim=(0,5))
ax3 = fig.add_subplot(313,xlim=(0,5))

ax1.scatter(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
ax2.scatter(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
ax3.scatter(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(series1, series2):
    covariance = 0
    mean1 = calc_mean(series1)
    mean2 = calc_mean(series2)
    for each1,each2 in zip(series1,series2):
        covariance += (each1 - mean1)*(each2 - mean2)
    covariance = covariance/len(series1)
    return covariance
    
rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(series1, series2):
    covariance = calc_covariance(series1,series2)
    std1 = calc_variance(series1)**(1/2)
    std2 = calc_variance(series2)**(1/2)
    correlation = covariance/(std1*std2)
    return correlation

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])