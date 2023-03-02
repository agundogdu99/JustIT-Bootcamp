from connect import *
from readMembers import *
from time import sleep


def delete():

    try:
        idField = input("Which Member ID do you want to delete?")
        # Selects the song with specific ID - idField
        cursor.execute(f"SELECT * FROM members where MemberID = {idField}")
        # Fethes the above selected record
        row = cursor.fetchone()

        if row == None:
            # row = idField
            print(f"No record with the Member ID {idField}")
        else:

            # Method 1
            cursor.execute(f"DELETE FROM members where MemberID = {idField}")
        # Method 2
        # cursor.execute("DELETE * FROM songs where songID =" + idField)
            conn.commit()

            # if cursor.rowcount == 0:
            #     raise ValueError(
            #         f"Error: No song with ID {idField} exists in the database.")

            sleep(3)
            read()

    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be deleted. Check that database and/or table exists: {e}")
        # sql.Error
        # Check out ExceptionGroup ==========================================


if __name__ == "__main__":
    delete()
