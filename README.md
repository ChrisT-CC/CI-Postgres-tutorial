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

*Disclaimer: this is a code along project from [Code Institute](https://codeinstitute.net/)'s **First look at an RDBMS ** module*