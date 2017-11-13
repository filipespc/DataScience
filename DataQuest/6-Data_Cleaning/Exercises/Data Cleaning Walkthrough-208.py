## 4. Reading in the Data ##

 import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for file in data_files:
    data[file[:-4]] = pd.read_csv("schools/"+file)

## 5. Exploring the SAT Data ##

print(data["sat_results"].head())

## 6. Exploring the Remaining Data ##

for key,value in data.items():
    print(value.head())
    print("-----------------------------------------------\n")

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv("schools/survey_all.txt",delimiter="\t",encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt",delimiter="\t",encoding="windows-1252")

survey = pd.concat([all_survey,d75_survey],axis=0)
survey.head()

## 9. Cleaning Up the Surveys ##

survey["DBN"] = survey["dbn"]
cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey[cols]
data["survey"] = survey

data["survey"].head()

## 11. Inserting DBN Fields ##

def pad2(data):
    if len(str(data.CSD)) == 1:
        return "0"+str(data.CSD)
        
data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]
data["class_size"]["padded_csd"] = data["class_size"].apply(pad2,axis=1)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"]+data["class_size"]["SCHOOL CODE"]

## 12. Combining the SAT Scores ##

data["sat_results"]["SAT Critical Reading Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Critical Reading Avg. Score"],errors="coerce")
data["sat_results"]["SAT Math Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Math Avg. Score"],errors="coerce")
data["sat_results"]["SAT Writing Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Writing Avg. Score"],errors="coerce")

data["sat_results"]["sat_score"] = data["sat_results"]["SAT Critical Reading Avg. Score"] + data["sat_results"]["SAT Math Avg. Score"] + data["sat_results"]["SAT Writing Avg. Score"]

data["sat_results"]["sat_score"].head()

## 13. Parsing Geographic Coordinates for Schools ##

import re

def str_parse_lat(string):
    return re.findall("\(.+\)",string)[0].replace("(","").replace(")","").split(", ")[0]

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(str_parse_lat)

data["hs_directory"].head()

## 14. Extracting the Longitude ##

import re

def str_parse_lon(string):
    return re.findall("\(.+\)",string)[0].replace("(","").replace(")","").split(", ")[1]

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(str_parse_lon)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"],errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"],errors="coerce")

data["hs_directory"].head()