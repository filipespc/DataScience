## 4. Querying a normalized database ##

cursor = conn.cursor()

q = "SELECT ceremonies.year, nominations.movie FROM nominations INNER JOIN ceremonies ON nominations.ceremony_id == ceremonies.id WHERE nominations.nominee == \"Natalie Portman\""
cursor.execute(q)

portman_movies = cursor.fetchall()

print(portman_movies)

## 7. Join table ##

cursor = conn.cursor()

q = "SELECT * FROM movies_actors LIMIT 5"
cursor.execute(q)
five_join_table = cursor.fetchall()

q = "SELECT * FROM actors LIMIT 5"
cursor.execute(q)
five_actors = cursor.fetchall()

q = "SELECT * FROM movies LIMIT 5"
cursor.execute(q)
five_movies = cursor.fetchall()

print(five_join_table)
print(five_actors)
print(five_movies)

## 9. Querying a many-to-many relation ##

cursor = conn.cursor()

q = "SELECT actors.actor,movies.movie FROM movies INNER JOIN movies_actors ON movies.id == movies_actors.movie_id INNER JOIN actors ON movies_actors.actor_id == actors.id WHERE movies.movie == \"The King's Speech\""

cursor.execute(q)
kings_actors = cursor.fetchall()

print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

cursor = conn.cursor()

q = "SELECT movies.movie, actors.actor FROM movies INNER JOIN movies_actors ON movies.id == movies_actors.movie_id INNER JOIN actors ON movies_actors.actor_id == actors.id WHERE actors.actor == \"Natalie Portman\""

portman_joins = cursor.execute(q).fetchall()

print(portman_joins)