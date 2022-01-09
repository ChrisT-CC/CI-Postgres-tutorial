# Import a few classes from within the sqlalchemy module
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Link Python file to Chinook database
# 3 slashes signifies that our database is hosted locally within
# workspace environment
# Executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

# The MetaData class will contain a collection of our table objects,
# and the associated data within those objects
meta = MetaData(db)

# Before we start to query the database, we need to construct our tables,
# so that Python knows the schema that we're working with.
# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Connect to the database, using the .connect() method, and
# the Python with-statement
# This saves our connection to the database into a variable called 'connection'
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 1 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(
    #     [artist_table.c.Name]
    # )

    # Query 3 - select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(
    #     artist_table.c.Name == "Queen"
    # )

    # Query 4 - select only "ArtistId" of '51' from the "Artist" table
    # select_query = artist_table.select().where(
    #     artist_table.c.ArtistId == 51
    # )

    # Query 5 - select all albums with "ArtistId" of '51'
    # from the "Album" table
    # select_query = album_table.select().where(
    #     album_table.c.ArtistId == 51
    # )

    # Query 6 - select all tracks from the "Track" table,
    # using the "Composer" of 'Queen'
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen"
    )

    results = connection.execute(select_query)
    for result in results:
        print(result)
