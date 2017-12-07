## 3. Psycopg2 ##

import psycopg2 as psc

conn = psc.connect("dbname=dq user=dq")
cur = conn.cursor()

print(cur)

conn.close()

## 4. Creating a table ##

import psycopg2 as psc

conn = psc.connect("dbname=dq user=dq")
cur = conn.cursor()

q = '''
    CREATE TABLE notes(
    id integer PRIMARY KEY,
    body text,
    title text
    )
'''

cur.execute(q)

conn.close()

## 5. SQL Transactions ##

import psycopg2 as psy

con = psy.connect("dbname=dq user=dq")
cur = con.cursor()

q = '''
    CREATE TABLE notes(
    id integer PRIMARY KEY,
    body text,
    title text
    )'''
cur.execute(q)
con.commit()

con.close()


## 6. Autocommitting ##

con = psycopg2.connect("dbname=dq user=dq")
cur = con.cursor()

con.autocommit = True

cur.execute("CREATE TABLE facts(id integer PRIMARY KEY, country text, value integer)")

con.close()

## 7. Executing queries ##

con = psycopg2.connect("dbname=dq user=dq")
cur = con.cursor()

q = "INSERT INTO notes VALUES (1,'Do more missions on Dataquest.','Dataquest reminder')"
cur.execute(q)

cur.execute("SELECT * FROM notes;")
print(cur.fetchall())

con.close()

## 8. Creating a database ##

con = psycopg2.connect("dbname=dq user=dq")
cur = con.cursor()

con.autocommit = True

cur.execute("CREATE DATABASE income OWNER dq")

con.close()

## 9. Deleting a database ##

con = psycopg2.connect("dbname=dq user=dq")
cur = con.cursor()

con.autocommit = True

cur.execute("DROP DATABASE income")

con.close()