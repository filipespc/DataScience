## 2. Calculating differences ##

female_diff = (10771 - 16280.5)/16280.5
male_diff = (21790 - 16280.5)/16280.5

## 3. Updating the formula ##

female_diff = (10771 - 16280.5)**2/16280.5
male_diff = (21790 - 16280.5)**2/16280.5
gender_chisq = female_diff + male_diff

## 4. Generating a distribution ##

import numpy as np

chi_squared_values = []

for _ in range(1000):
    rand_array = np.random.random((32561,))
    male_freq = (rand_array > 0.5).sum()
    female_freq = (rand_array <= 0.5).sum()
    
    male_diff = (male_freq-16280.5)**2/16280.5
    female_diff = (female_freq-16280.5)**2/16280.5
    
    chi_squared_values.append(male_diff + female_diff)
    
plt.hist(chi_squared_values)
    


## 6. Smaller samples ##

female_diff = (107.71-162.805)**2/162.805
male_diff = (217.90-162.805)**2/162.805

gender_chisq = male_diff + female_diff

## 7. Sampling distribution equality ##

import numpy as np

chi_squared_values = []

for _ in range(1000):
    rand_array = np.random.random((300,))
    male_freq = (rand_array >= 0.5).sum()
    female_freq = (rand_array < 0.5).sum()
    
    male_diff = (male_freq-150)**2/150
    female_diff = (female_freq-150)**2/150
    
    chi_squared_values.append(male_diff+female_diff)
    
plt.hist(chi_squared_values)

## 9. Increasing degrees of freedom ##

diff_list = []
diff_list.append((27816-26146.5)**2/26146.5)
diff_list.append((3124-3939.9)**2/3939.9)
diff_list.append((1039-944.3)**2/944.3)
diff_list.append((311-260.5)**2/260.5)
diff_list.append((271-1269.8)**2/1269.8)

race_chisq = np.sum(diff_list)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

obs = [27816, 3124, 1039, 311, 271]
exp = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

race_pvalue = chisquare(obs,exp)