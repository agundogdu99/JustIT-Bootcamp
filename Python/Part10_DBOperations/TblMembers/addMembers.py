from connect import *
from time import sleep
from readMembers import *

# Define function


def insertMembers():
    # Create an empty list
    members = []

    # Ask user for input
    # songID not required because it is auto_increment
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    email = input("Enter Email address: ")

    # Append data captured from user input in to the songs list
    members.append(firstName)
    members.append(lastName)
    members.append(email)

    # Insert INTO songs (title artist genre) VALUE ("A", "B", "C")
    "   OR  "
    # Insert INTO songs VALUE (NULL, "A", "B", "C")

    try:  # Read into SQL injection - to prevent hacking
        cursor.execute("INSERT INTO members VALUES (NULL, ?, ?, ?)", members)
        conn.commit()  # Make the changes permanent
        print(f"{firstName} {lastName} added in the members table")

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
    insertMembers()
