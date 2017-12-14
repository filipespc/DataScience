from read import load_data
from collections import Counter as ct
import pandas as pd

def remove_subdomain(url):
    urls = url.split(".")
    if len(urls) < 2:
        return url
    if (urls[-2] == "com") | (urls[-2] == "co"):
        url = urls[-3]+"."+urls[-2]+"."+urls[-1]
    else:
        url = urls[-2]+"."+urls[-1]

    return url

if __name__ == "__main__":
    data = load_data()
    
    data.loc[pd.isnull(data["url"]),"url"] = ""
    data["url"] = data["url"].apply(remove_subdomain)
    
    domains_count = data["url"].value_counts()
    
    i = 0
    for url, count in domains_count.items():
        i += 1
        print("{} - {}: {}".format(i, url, count))
        if i >= 20:
            break