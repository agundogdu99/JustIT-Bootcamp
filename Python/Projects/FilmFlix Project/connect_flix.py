import sqlite3 as sql  # import the sqlite module

# Create a connection object that represents the database you want to create and/or use

# To use the modile, start by creating a database object:
try:
    with sql.connect("Python/Projects/FilmFlix Project/filmflix.db") as conn:
        # Once connection is established,
        # Create a cursor object and call its execute() method to perform sql queries
        cursor = conn.cursor()
except sql.OperationalError as e:
    print(f"Connection Failed {e}")
