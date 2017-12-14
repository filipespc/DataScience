from read import load_data
from collections import Counter as ct
import pandas as pd


if __name__ == "__main__":
    data = load_data()
    full_str = " "
    data.loc[pd.isnull(data["headline"]),"headline"] = ""
    full_str = full_str.join(data["headline"]).lower()
    words = full_str.split()
    print(ct(words).most_common()[:100])
    