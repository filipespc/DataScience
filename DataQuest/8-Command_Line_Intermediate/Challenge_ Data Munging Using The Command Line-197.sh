## 1. Data munging ##

/home/dq$ ls -l

## 2. Data exploration ##

/home/dq$ head -n 10 Hud_2005.csv Hud_2007.csv Hud_2013.csv

## 3. Filtering ##

/home/dq$ tail -n 46853 Hud_2005.csv >> combined_hud.csv

## 4. Consolidating datasets ##

/home/dq$ tail -n 64535 Hud_2013.csv >> combined_hud.csv

## 5. Counting ##

/home/dq$ cat combined_hud.csv | grep "1980-1989" | wc -l