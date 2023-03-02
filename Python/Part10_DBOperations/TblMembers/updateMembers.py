from connect import *
from readMembers import *
from time import sleep


def update():
    try:
        idField = input("Which song ID do you want to update? ")

        cursor.execute(f"SELECT * FROM songs where songID = {idField}")
        # Fethes the above selected record
        row = cursor.fetchone()

        if row == None:
            print(f"No record with the song ID {idField}")
        else:

            fieldName = input(
                "Which field do you want to update? (Title, Artist or Genre): "
            ).title()
            newFieldValue = input(
                f"Enter the value for the {fieldName} field: ")

            print(
                f"This is the new field value as was entered {newFieldValue}")
            newFieldValue = "'" + newFieldValue + "'"
            print(
                f"This is the new field value as was amended {newFieldValue}")

            # Selects the song with specific ID - idField
            cursor.execute(
                f"UPDATE songs SET {fieldName} = {newFieldValue} WHERE songID = {idField}"
            )
            # Fethes the above selected record
            conn.commit()
            print(f"Record with SongID {idField} updated")
            sleep(3)
            read()
    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be updated. Check that database and/or table exists: {e}"
        )

        # if row == None:
        #     # row = idField
        #     print(f"No record with the song ID {idField}")
        # else:


if __name__ == '__main__':
    update()
