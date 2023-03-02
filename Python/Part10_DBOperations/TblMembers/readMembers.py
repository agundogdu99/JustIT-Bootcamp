from connect import *


def read():
    try:
        cursor.execute("SELECT * FROM members")  # Selects all records
        row = cursor.fetchall()  # Get all the selected records
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Error, Record cannot be read: {e}")


if __name__ == "__main__":
    read()
