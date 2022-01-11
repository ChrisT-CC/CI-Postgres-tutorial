# Import a few classes from within the sqlalchemy module

from sqlalchemy import (
    create_engine, Column, Integer, String, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Link Python file to Chinook database
# Executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
# 'base' class will essentially grab the metadata that is produced by database
# table schema, and creates a subclass to map everything back to us,
# here within the 'base' variable
base = declarative_base()

# Create a class-based model for the "Country" table
class Country(base):
    __tablename__ = "Country"
    Rank = Column(Integer, primary_key=True)
    Name = Column(String)
    Capital_city = Column(String)
    Population = Column(Float)
    Surface_area = Column(String)
    Description = Column(String)

# Instead of connecting to the db directly, we will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# In order to connect to the database, we have to call Session()
# and open an actual session by calling the Session() subclass define above
session = Session()

# Create the db using declarative_base subclass
base.metadata.create_all(db)

# Create records on "Country" table
Canada = Country(
    Name = "Canada",
    Capital_city = "Ottawa",
    Population = 37.6,
    Surface_area = "9.985 million km²",
    Description = "Canada takes up about two-fifths of the North American continent, making it the second-largest country in the world after Russia. The country is sparsely populated. Canada’s expansive wilderness to the north plays a large role in Canadian identity, as does the country’s reputation of welcoming immigrants."
)

Denmark = Country(
    Name = "Denmark",
    Capital_city = "Copenhagen",
    Population = 5.81,
    Surface_area = "42,933 km²",
    Description = "The Kingdom of Denmark emerged in the 10th century and includes two North Atlantic island nations, the Faroe Islands and Greenland. Along with Sweden and Norway, it forms Scandinavia, a cultural region in Northern Europe."
)

Sweden = Country(
    Name = "Sweden",
    Capital_city = "Stockholm",
    Population = 10.35,
    Surface_area = "450,295 km²",
    Description = "The Kingdom of Sweden, flanked by Norway to the west and the Baltic Sea to the east, expands across much of the Scandinavian Peninsula and is one of the largest countries in the European Union by land mass. Capital city Stockholm was claimed in the 16th century, and border disputes through the Middle Ages established the modern-day nation."
)

Norway = Country(
    Name = "Norway",
    Capital_city = "Oslo",
    Population = 5.379,
    Surface_area = "385,207 km²",
    Description = "The Kingdom of Norway is the westernmost country in the Scandinavian peninsula, made up mostly of mountainous terrain. Nearly all of its population lives in the south, surrounding the capital, Oslo. Norway’s coastline is made up of thousands of miles of fjords, bays and island shores. The Norwegians developed a maritime culture, and were active throughout the Viking era, establishing settlements in Iceland and Greenland."
)

Switzerland = Country(
    Name = "Switzerland",
    Capital_city = "Bern",
    Population = 8.637,
    Surface_area = "41,285 km²",
    Description = "Switzerland, officially called the Swiss Federation, is a small country in Central Europe made up of 16,000 square miles of glacier-carved Alps, lakes and valleys. It’s one of the world’s wealthiest countries, and has been well-known for centuries for its neutrality."
)

# Add each country instance to the session
# session.add(Canada)
# session.add(Denmark)
# session.add(Sweden)
# session.add(Norway)
# session.add(Switzerland)

# Updating a single record

# Updating multiple records

# Deleting a single record

# Deleting multiple records

# Commit session to the database
session.commit()

# Query the database to find all countries
countries = session.query(Country)
for country in countries:
    print(
        country.Rank,
        country.Name,
        country.Capital_city,
        country.Population,
        " millions",
        country.Surface_area,
        country.Description,
        sep=" | "
    )