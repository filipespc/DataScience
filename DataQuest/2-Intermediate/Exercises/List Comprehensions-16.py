## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for idx, ship in enumerate(ships):
    print(ship)
    print(cars[idx])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for idx, thing in enumerate(things):
    thing.append(trees[idx])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [price*2 for price in apple_prices]
apple_prices_lowered = [price-100 for price in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for each in legislators:
    if each[3] == "F" and each[7] > 1940:
        if each[1] in name_counts:
            name_counts[each[1]] += 1
        else:
            name_counts[each[1]] = 1

print(name_counts)

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for each in values:
    checks.append(each is not None and each > 30)

## 8. Highest Female Name Count ##

max_value = None

for each in name_counts:
    count = name_counts[each]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for plant, plant_type in plant_types.items():
    print(plant)
    print(plant_type)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for name,count in name_counts.items():
    if count == 2:
        top_female_names.append(name)

## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = {}
for each in legislators:
    if each[3] == "M" and each[7] > 1940:
        if each[1] in male_name_counts:
            male_name_counts[each[1]] += 1
        else:
            male_name_counts[each[1]] = 1

highest_male_count = None
for name,count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

for name,count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)