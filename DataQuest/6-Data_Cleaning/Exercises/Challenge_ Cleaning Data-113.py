## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")

avengers.head(5)



## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers['Year']>=1960]

## 5. Consolidating Deaths ##

def count_deaths(avenger):
    death_count=0
    death_fields = ["Death1","Death2","Death3","Death4","Death5"]
    for death in death_fields:
        if avenger[death] == "YES":
            death_count += 1
    return death_count

true_avengers["Deaths"] = true_avengers.apply(count_deaths,axis=1)
true_avengers.head()
        


## 6. Verifying Years Since Joining ##

joined_accuracy_count  = (true_avengers["Years since joining"] == 2015-true_avengers["Year"]).sum()