# import os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)
from connect import *


def read():
    try:
        cursor.execute("SELECT * FROM songs")  # Selects all records
        row = cursor.fetchall()  # Get all the selected records
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Error, Record cannot be read: {e}")


if __name__ == "__main__":
    read()
