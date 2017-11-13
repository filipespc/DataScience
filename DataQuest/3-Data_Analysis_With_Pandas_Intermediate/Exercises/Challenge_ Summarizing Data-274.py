## 2. Introduction to the Data ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
all_ages.head(5)
recent_grads.head(5)

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_lst = all_ages["Major_category"].unique()
aa_cat_counts = dict()

for cat in aa_cat_lst:
    is_a_match = (all_ages['Major_category'] == cat)
    total = all_ages["Total"][is_a_match].sum()
    aa_cat_counts[cat] = total

rg_cat_lst = recent_grads["Major_category"].unique()
rg_cat_counts = dict()

for cat in rg_cat_lst:
    is_a_match = (recent_grads['Major_category'] == cat)
    total = recent_grads["Total"][is_a_match].sum()
    rg_cat_counts[cat] = total


## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_proportion = recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum()
print(low_wage_proportion)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for maj in majors:
    aa_maj_match = (all_ages["Major"] == maj)
    rg_maj_match = (recent_grads["Major"] == maj)
    aa_unmpl = all_ages["Unemployment_rate"][aa_maj_match].sum()
    rg_unmpl = recent_grads["Unemployment_rate"][rg_maj_match].sum()
    if rg_unmpl < aa_unmpl:
        rg_lower_count += 1
        
display(rg_lower_count)