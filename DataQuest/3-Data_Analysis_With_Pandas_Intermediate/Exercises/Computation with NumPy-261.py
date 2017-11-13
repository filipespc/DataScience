## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0] == "1984"

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = ((world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria"))
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

world_alcohol_1986 = (world_alcohol[:,0] == "1986")
world_alcohol[world_alcohol_1986,0] = "2014"
world_alcohol_wine = (world_alcohol[:,3] == "Wine")
world_alcohol[world_alcohol_wine,3] = "Grog"

## 6. Replacing Empty Strings ##

is_value_empty = (world_alcohol[:,4] == "")
world_alcohol[is_value_empty,4] = "0"

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4].astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = ((world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada"))
canada_1986 = world_alcohol[is_canada_1986,:]

canada_alcohol = canada_1986[:,4]
canada_alcohol[canada_alcohol == ""] = "0"
canada_alcohol = canada_alcohol.astype(float)

total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
year = "1989"

for country in countries:
    is_a_match = ((world_alcohol[:,0] == year) & (world_alcohol[:,2] == country))
    consumption = world_alcohol[is_a_match,4]
    consumption[consumption == ""] = "0"
    consumption = consumption.astype(float)
    totals[country] = consumption.sum()

totals

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

for country,consumption in totals.items():
    if consumption > highest_value:
        highest_value = consumption
        highest_key = country