# PostgreSQL tutorial

This is a [Code Institute](https://codeinstitute.net/) code along project designed to learn:
- how to use Postgres in its native form through the command-line interface.
- how to use helpful Python adapters to perform those same queries.
- how to execute queries programmatically from within the Python files.

---

## Installing the Chinook Database

### 1. Download the Chinook PostgreSql database
- [source](https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql)
- `wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql`

### 2. Access the Postgres CLI
- `psql`

*Warning* - If you get the following error after typing psql in the terminal:

`psql: error: could not connect to server: No such file or directory`

The following command must be used in the terminal to set an environment variable needed for it to work:

`set_pg`

### 3. Create the new "chinook" database
- `CREATE DATABASE chinook;`

### 4. View existing tables on the database
- `\l`

### 5. Switch between databases
- `\c postgres` (switch to the database called "postgres")
- `\c chinook` (switch to the database called "chinook")

### 6. Install / Initialize the downloaded Chinook SQL database
- `\i Chinook_PostgreSql.sql` (takes several minutes)

---

## PostgreSQL from the Command Line

### Quit the entire Postgres CLI
- `\q`

### Connect to the "chinook" Postgres CLI database
- `set_pg`
- `psql -d chinook`

### Display all tables on the "chinook" database
- `\dt`

### Quit the query / return back to CLI after a query
- `q`

### Retrieve all data from the "Artist" table
- `SELECT * FROM "Artist";`

### Retrieve only the "Name" column from the "Artist" table
- `SELECT "Name" FROM "Artist";`

### Retrieve only "Queen" from the "Artist" table
- `SELECT * FROM "Artist" WHERE "Name" = 'Queen';`

### Retrieve only "Queen" from the "Artist" table, but using the "ArtistId" of '51'
- `SELECT * FROM "Artist" WHERE "ArtistId" = 51;`

### Retrieve all albums from the "Album" table, using the "ArtistId" of '51'
- `SELECT * FROM "Album" WHERE "ArtistId" = 51;`

### Retrieve all tracks from the "Track" table, using the "Composer" of 'Queen'
- `SELECT * FROM "Track" WHERE "Composer" = 'Queen';`

---

## OPTIONAL

### Copy the results into a .CSV file
- `\copy (SELECT * FROM "Track" WHERE "Composer" = 'Queen') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;`

### Copy the results into a .JSON file
- Line 1: `\o test.json`
- Line 2: `SELECT json_agg(t) FROM  (SELECT * FROM "Track" WHERE "Composer" = 'Queen') t;`

---

## Installing the Libraries and Setting Up

### Install the "psycopg2" Python package
- `pip3 install psycopg2`

### Create a new file: "sql-psycopg2.py"
- `touch sql-psycopg2.py`

---


*Disclaimer: this is a code along project from [Code Institute](https://codeinstitute.net/)'s **First look at an RDBMS ** module*