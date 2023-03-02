from connect import *
from time import sleep
from readSongs import *


# Define function


def insertSongs():
    # Create an empty list
    songs = []

    # Ask user for input
    # songID not required because it is auto_increment
    title = input("Enter Song Title: ")
    artist = input("Enter Artist Name: ")
    genre = input("Enter Song Genre: ")

    # Append data captured from user input in to the songs list
    songs.append(title)
    songs.append(artist)
    songs.append(genre)

    # Insert INTO songs (title artist genre) VALUE ("A", "B", "C")
    "   OR  "
    # Insert INTO songs VALUE (NULL, "A", "B", "C")

    try:        # Read into SQL injection - to prevent hacking
        cursor.execute("INSERT INTO songs VALUES (NULL, ?, ?, ?)", songs)
        conn.commit()  # Make the changes permanent
        print(f"{title} added in the songs table")

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
    insertSongs()
