from read import load_data
import dateutil
import pandas as pd

def get_hour(time):
    return dateutil.parser.parse(time).hour

def get_month(time):
    return dateutil.parser.parse(time).month

def get_year(time):
    return dateutil.parser.parse(time).year

def get_week_day(time):
    return dateutil.parser.parse(time).weekday()



if __name__ == "__main__":
    data = load_data()
    
    print("Hours:")
    submission_hours_count = data["submission_time"].apply(get_hour).value_counts()
    print(submission_hours_count)

    print("------------------------\n")
    print("Months:")
    submission_months_count = data["submission_time"].apply(get_month).value_counts()
    print(submission_months_count)

    print("------------------------\n")
    print("Years:")
    submission_years_count = data["submission_time"].apply(get_year).value_counts()
    print(submission_years_count)
    
    print("------------------------\n")
    print("Week day:")
    submission_week_day_count = data["submission_time"].apply(get_week_day).value_counts()
    print(submission_week_day_count)