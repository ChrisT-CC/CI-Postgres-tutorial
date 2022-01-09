import psycopg2


# Connect to "chinook" database using connect() method, without additional
# connection values such as host, username, password, and so on
connection = psycopg2.connect(database="chinook")


# Build a cursor object of the database (set or list)
cursor = connection.cursor()


# Query 1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')


# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')


# Query 3 - select only "Queen" from the "Artist" table
# %s is a Python string placeholder, define the desired string within a list
# You can have multiple placeholders, depending on how detailed the query needs
# to be, and each placeholder would be added to this list
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])


# Query 4 - select only "ArtistId" of '51' from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])


# Query 5 - select all albums with "ArtistId" of '51' from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])


# Query 6 - select all tracks from the "Track" table,
# using the "Composer" of 'Queen'
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# Fetch the results (multiple)
results = cursor.fetchall()


# Fetch the results (single)
# results = cursor.fetchone()


# Close the connection
connection.close()


# Print results
for result in results:
    print(result)
