## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags.loc[flags["bars"].idxmax(),"name"]
highest_population_country = flags.loc[flags["population"].idxmax(),"name"]

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = (flags["orange"]==1).sum()/total_countries
stripe_probability = (flags["stripes"]>1).sum()/total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = .5 ** 10
hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total_countries = flags.shape[0]

red_count = (flags["red"] == 1).sum()

three_red = red_count/total_countries * (red_count-1)/(total_countries-1) * (red_count-2)/(total_countries-2)

## 5. Disjunctive probability ##

start = 1
end = 18000
total_range = range(start,end+1)

import numpy as np
hundred_prob = ((np.asarray(total_range) % 100) == 0).sum()/len(total_range)
seventy_prob = ((np.asarray(total_range) % 70) == 0).sum()/len(total_range)

## 6. Disjunctive dependent probabilities ##

red_or_orange = ((flags["orange"] == 1) | (flags["red"] == 1)).sum()/flags.shape[0]
stripes_or_bars = ((flags["stripes"] >= 1) | (flags["bars"] >= 1)).sum()/flags.shape[0]

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = 1-(0.5**3)