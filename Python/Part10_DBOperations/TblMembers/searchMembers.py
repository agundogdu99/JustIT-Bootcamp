from connect import *
from readMembers import *
from time import sleep


def search():
    try:
        field = input(
            "Would you like to search by MemberID/Firstname/Lastname/Email? "
        ).title()

        if field == "Memberid":
            idInput = input("Enter Member ID: ")
            cursor.execute(f"SELECT * FROM members where memberID = {idInput}")
            row = cursor.fetchone()
            if row == None:
                print(f"No record with the Member ID {idInput}")
            else:
                print(row)

        elif field == "Firstname" or field == "Lastname" or field == "Email":
            searchInput = input(f"Enter Search field for {field}: ")
            cursor.execute(
                f"SELECT * FROM members where {field} LIKE '%{searchInput}%'")
            rows = cursor.fetchall()
            if rows == None:
                print(f"No record with {field} matching '{searchInput}'")
            else:
                for row in rows:
                    print(row)
        else:
            print("Invalid search field.")

        sleep(3)
        read()
    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be updated. Check that database and/or table exists: {e}"
        )

    if __name__ == '__main__':
        search()


# def search():
#     try:
#         field = input(
#             "Would you like to search by SongID.Title/Artist/Genre? ").title()

#         if field == "SongID":
#             idInput = input("Enter Song ID: ")
#             cursor.execute(f"SELECT * FROM songs where songID = {idInput}")
#             row = cursor.fetchone()
#             if row == None:
#                 print(f"No record with the song ID {idInput}")
#             else:
#                 print(row)

#         elif field == "Artist" or field == "Title" or field == "Genre":
#             searchInput = input(f"Enter Search field for {field}: ")
#             cursor.execute(
#                 f"SELECT * FROM songs where {field} LIKE '%{searchInput}%'")
#             rows = cursor.fetchall()
#             if rows == None:
#                 print(f"No record with {field} matching '{searchInput}'")
#             else:
#                 for row in rows:
#                     print(row)
#         else:
#             print("Invalid search field.")
