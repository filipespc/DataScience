## 1. Overview ##

f = open("movie_metadata.csv","r")
movie_data_raw = f.read()
movie_data_rows = movie_data_raw.split("\n")
movie_data = []

for element in movie_data_rows:
    movie_data.append(element.split(","))

print(movie_data[0:5])

## 3. Writing Our Own Functions ##

def first_col(movie_data_p):
    movie = []
    for element in movie_data_p:
        movie.append(element[0])
    return movie

movie_names = first_col(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

def parse_csv(csv_string):
    csv_rows = csv_string.split("\n")
    csv_parsed = []
    for element in csv_rows:
        csv_parsed.append(element.split(","))
    return csv_parsed
                          
def is_usa(movie):
    if movie[6] == "USA":
        return True
    else:
        return False

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
f = open("movie_metadata.csv","r")
movie_data = parse_csv(f.read())

first_USA = is_usa(movie_data[0])
second_USA = is_usa(movie_data[1])
third_USA = is_usa(movie_data[2])

wonder_woman_usa = is_usa(wonder_woman)



## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

def index_equals_str(input_lst, index, string):
    if input_lst[index] == string:
        return True
    else:
        return False

print(index_equals_str(wonder_woman, 2, "Color"))
print(index_equals_str(wonder_woman, 3, 117))
print(index_equals_str(index = 2, string = "Color", input_lst = wonder_woman))

wonder_woman_in_color = index_equals_str(wonder_woman, string = "Color", index = 2)
print(wonder_woman_in_color)

## 6. Optional Arguments ##

def parse_csv(csv_string):
    csv_rows = csv_string.split("\n")
    csv_parsed = []
    for element in csv_rows:
        csv_parsed.append(element.split(","))
    return csv_parsed

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst,col,input_str):
    num_elt = 0
    for element in input_lst:
        if index_equals_str(element,col,input_str):
            num_elt += 1
    return num_elt

f = open("movie_metadata.csv","r")
movie_data = parse_csv(f.read())

num_of_us_movies = feature_counter(movie_data, 6, "USA")
print(num_of_us_movies)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst):
    statistics = {}
    statistics["japan_films"] = feature_counter(input_lst,6,"Japan",True)
    statistics["color_films"] = feature_counter(input_lst,2,"Color",True)
    statistics["films_in_english"] = feature_counter(input_lst,5,"English",True)
    return statistics

summary = summary_statistics(movie_data)