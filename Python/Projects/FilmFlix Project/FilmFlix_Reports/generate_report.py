from time import sleep
from connect_flix import *


def report_result(field):
    report_param = input(f"Enter your Search Parameter for {field.title()}: ")
    if field == "title" or field == "rating" or field == "genre":
        cursor.execute(
            f"SELECT * FROM tblfilms where {field} LIKE '%{report_param}%'")
        rows = cursor.fetchall()
    elif field == "duration" or field == "yearReleased":
        cursor.execute(
            f"SELECT * FROM tblfilms where {field} <= {report_param}")
        rows = cursor.fetchall()
    elif field == "YearReleased" or field == "Duration":
        cursor.execute(
            f"SELECT * FROM tblfilms where {field} >= {report_param}")
        rows = cursor.fetchall()
    if rows == None:
        print(f"No record with {field} matching '{report_param}'")
    else:
        for row in rows:
            print(row)
        else:
            print("Invalid search field.")
    report_again = input(
        "Would You like to generate another report? Enter Y or N: ").upper()
    if report_again == "Y":
        report_menu()


def id_report_result(field):
    report_param = input(f"Enter your Search Parameter for {field.title()}: ")
    cursor.execute(f"SELECT * FROM tblFilms where filmID = {report_param}")
    row = cursor.fetchone()
    if row == None:
        print(f"No record with the Title ID {field}")
        report_again = input(
            "Would You like to generate another report? Enter Y or N: ").upper(
            )
        if report_again == "Y":
            report_menu()
    else:
        print(row)
        report_again = input(
            "Would You like to generate another report? Enter Y or N: ").upper(
            )
        if report_again == "Y":
            report_menu()


def report_menu():
    try:
        report_field = input("""
                             What area would you like to generate a report on?
                             1 - Film ID
                             2 - Title
                             3 - Earliest Release Year
                             4 - Latest Release Year
                             5 - Rating
                             6 - Minimum Duration
                             7 - Maximum Duration
                             8 - Genre
                             Enter Value: """)
        if report_field == "1":
            field = "titleID"
            id_report_result(field)
        elif report_field == "2":
            field = "title"
            report_result(field)
        elif report_field == "3":
            field = "YearReleased"
            report_result(field)
        elif report_field == "4":
            field = "yearReleased"
            report_result(field)
        elif report_field == "5":
            field = "rating"
            report_result(field)
        elif report_field == "6":
            field = "Duration"
            report_result(field)
        elif report_field == "7":
            field = "duration"
            report_result(field)
        elif report_field == "8":
            field = "genre"
            report_result(field)
    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be updated. Check that database and/or table exists: {e}"
        )

    if __name__ == '__main__':
        report_menu()