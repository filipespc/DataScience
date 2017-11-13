## 1. The Time Module ##

import time

current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime

print(datetime.datetime)
current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(month = 3, day = 22, year = 2233)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime

for post in posts:
    try:
        post[2] = datetime.datetime.fromtimestamp(float(post[2]))
    except Exception:
        post[2] = datetime.datetime.fromtimestamp(0)

## 9. Counting Posts from March ##

march_count = 0

for post in posts:
    if post[2].month == 3:
        march_count += 1
        
print(march_count)

## 10. Counting Posts from Any Month ##

def month_posts_count(posts, month):
    month_count = 0
    for post in posts:
        if post[2].month == month:
            month_count += 1
    return month_count

feb_count = month_posts_count(posts, 2)
aug_count = month_posts_count(posts, 8)