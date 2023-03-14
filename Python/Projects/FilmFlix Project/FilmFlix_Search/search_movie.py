from time import sleep
from connect_flix import *


def search_result(field):
    search_param = input(f"Enter your Search Parameter for {field.title()}: ")
    if field == "title" or field == "yearReleased" or field == "rating" or field == "genre":
        cursor.execute(
            f"SELECT * FROM tblfilms where {field} LIKE '%{search_param}%'")
        rows = cursor.fetchall()
    elif field == "duration":
        cursor.execute(
            f"SELECT * FROM tblfilms where {field} = {search_param}")
        rows = cursor.fetchall()
    if rows == None:
        print(f"No record with {field} matching '{search_param}'")
    else:
        for row in rows:
            print(row)
        else:
            print("Invalid search field.")
    search_again = input(
        "Would You like to add Search again? Enter Y or N: ").upper()
    if search_again == "Y":
        search_movie()


def id_search_result(field):
    search_param = input(f"Enter your Search Parameter for {field.title()}: ")
    cursor.execute(f"SELECT * FROM tblFilms where filmID = {search_param}")
    row = cursor.fetchone()
    if row == None:
        print(f"No record with the Title ID {field}")
    else:
        print(row)
    search_again = input(
        "Would You like to add Search again? Enter Y or N: ").upper()
    if search_again == "Y":
        search_movie()


def search_movie():
    try:
        search_field = input("""
                             What search field would you like to search by?
                             1 - Film ID
                             2 - Title
                             3 - Release Year
                             4 - Rating
                             5 - Duration
                             6 - Genre
                             Enter Value: """)
        if search_field == "1":
            field = "titleID"
            id_search_result(field)
        elif search_field == "2":
            field = "title"
            search_result(field)
        elif search_field == "3":
            field = "yearReleased"
            search_result(field)
        elif search_field == "4":
            field = "rating"
            search_result(field)
        elif search_field == "5":
            field = "duration"
            search_result(field)
        elif search_field == "6":
            field = "genre"
            search_result(field)

    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be updated. Check that database and/or table exists: {e}"
        )

    if __name__ == '__main__':
        search_movie()