## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

plt.plot(unrate[0:12]["DATE"],unrate[0:12]["VALUE"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
plt1 = fig.add_subplot(2,1,1)
plt2 = fig.add_subplot(2,1,2)
plt1.plot(unrate[:12]["DATE"],unrate[:12]["VALUE"])
plt2.plot(unrate[12:24]["DATE"],unrate[12:24]["VALUE"])
plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

fig = plt.figure(figsize=(12,12))

subplot_count = 5

sub_plt = []
for i in list(range(subplot_count)):
    sub_plt.append(fig.add_subplot(subplot_count,1,i+1))
    sub_plt[i].plot(unrate[i*12:i*12+12]["DATE"],unrate[i*12:i*12+12]["VALUE"])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,3))

subplot_count = 2
color_list = ["red","blue"]

sub_plt = []
for i in list(range(subplot_count)):
    print(i)
    plt.plot(unrate[i*12:i*12+12]["MONTH"],unrate[i*12:i*12+12]["VALUE"], c=color_list[i])

plt.show()

## 9. Adding More Lines ##

fig = plt.figure(figsize=(10,6))

subplot_count = 5
color_list = ["red","blue","green","orange","black"]

sub_plt = []
for i in list(range(subplot_count)):
    plt.plot(unrate[i*12:i*12+12]["MONTH"],unrate[i*12:i*12+12]["VALUE"], c=color_list[i])
    
plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
traces = [['red','1948'], ['blue','1949'], ['green','1950'], ['orange','1951'], ['black','1952']]
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=traces[i][0], label=traces[i][1])
    
plt.legend(loc='upper left')
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')

plt.title("Montly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")

plt.show()