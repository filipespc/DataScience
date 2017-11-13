## 2. Parsing the File ##

f = open("la_weather.csv", "r")

raw_data = f.read()
row_data = raw_data.split("\n")
weather_data = []

for data in row_data:
    weather_data.append(data.split(","))

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for element in weather_data:
    weather.append(element[1])

## 4. Counting the Items in a List ##

count = 0

for element in weather:
    count += 1

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for element in weather_types:
    weather_type_found.append(element in new_weather)