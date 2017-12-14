## 2. Calculating expected values ##

males_p = 0.669
females_p = 1-males_p
over50k_p = 0.241
under50k_p = 1-over50k_p
population = 32561

males_over50k = males_p*over50k_p*population
males_under50k = males_p*under50k_p*population
females_over50k = females_p*over50k_p*population
females_under50k = females_p*under50k_p*population


## 3. Calculating chi-squared ##

from scipy.stats import chisquare as chi_sq

obs = [6662,1179,15128,9592]
exp = [5249.8,2597.4,16533.5,8180.3]

chisq_gender_income,_ = chi_sq(obs,exp)

## 4. Finding statistical significance ##

from scipy.stats import chisquare as chi_sq

obs = [6662,1179,15128,9592]
exp = [5249.8,2597.4,16533.5,8180.3]

chisq_gender_income,pvalue_gender_income = chi_sq(obs,exp)

## 5. Cross tables ##

import pandas as pd

table = pd.crosstab(income["sex"],[income["race"]])
print(table)

## 6. Finding expected values ##

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

_,pvalue_gender_race,_,_ = chi2_contingency(pd.crosstab(income["sex"],[income["race"]]))