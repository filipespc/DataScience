## 3. Read the File Into a String ##

file = open("dq_unisex_names.csv","r")
names = file.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []

for name in names_list:
    nested_list.append(name.split(','))
    
print(nested_list[0:5])

## 6. Convert Numerical Values ##

print(nested_list[0:5])

numerical_list = []

for element in nested_list:
    numerical_list.append([element[0], float(element[1])])
    
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []

for element in numerical_list:
    if element[1] >= 1000:
        thousand_or_greater.append(element[0])

print(thousand_or_greater[0:10])