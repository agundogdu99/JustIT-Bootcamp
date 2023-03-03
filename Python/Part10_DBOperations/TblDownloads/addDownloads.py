from connect import *
from time import sleep
from readDownloads import *

# Define function


def insertDownloads():
    # Create an empty list
    downloads = []

    # Ask user for input
    # songID not required because it is auto_increment
    songID = input("Enter Song ID: ")
    memberID = input("Enter Member ID: ")
    date = input("Enter Date (dd/mm/yyyy): ")

    # Append data captured from user input in to the songs list
    downloads.append(songID)
    downloads.append(memberID)
    downloads.append(date)

    # Insert INTO songs (title artist genre) VALUE ("A", "B", "C")
    "   OR  "
    # Insert INTO songs VALUE (NULL, "A", "B", "C")

    try:  # Read into SQL injection - to prevent hacking
        cursor.execute("INSERT INTO downlods VALUES (NULL, ?, ?, ?)",
                       downloads)
        conn.commit()  # Make the changes permanent
        print(
            f"Song ID {songID}, Member ID {memberID} added in the Downloads table"
        )

        # Delay for 3 seconds, then read all the data from the songs table
        sleep(3)
        read()  # Call the read() function from the external readSongs.py file
        # cursor.execute("SELECT * FROM songs")  # Selects all records
        # row = cursor.fetchall()  # Get all the selected records
        # for aRecord in row:
        #     print(aRecord)
    except sql.OperationalError as e:
        print(f"Error, Record not inserted: {e}")


if __name__ == "__main__":
    insertDownloads()
