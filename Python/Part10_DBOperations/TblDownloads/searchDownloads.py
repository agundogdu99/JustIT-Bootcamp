from connect import *
from readDownloads import *
from time import sleep


def search():
    try:
        field = input(
            "Would you like to search by DownloadID/SongID/MemberID/Date? "
        ).title()

        if field == "Downloadid":
            idInput = input("Enter Download ID: ")
            cursor.execute(
                f"SELECT * FROM downloads where downlID = {idInput}")
            row = cursor.fetchone()
            if row == None:
                print(f"No record with the Download ID {idInput}")
            else:
                print(row)

        elif field == "Songid" or field == "Memberid" or field == "Date":
            searchInput = input(f"Enter Search field for {field}: ")
            cursor.execute(
                f"SELECT * FROM downloads where {field} LIKE '%{searchInput}%'"
            )
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
