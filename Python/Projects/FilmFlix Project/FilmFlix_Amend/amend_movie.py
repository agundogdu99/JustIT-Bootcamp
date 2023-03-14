from connect_flix import *
from time import sleep


def amend_movie():
    try:
        film_id = input("Enter the ID of the Film you want to amend... ")
        cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {film_id}")
        row = cursor.fetchone()
        if row == None:
            print(f"No Film with the ID {film_id} exists...")
        else:
            field_to_change = input("""
                                    What Field would you like to change?
                                    1 - Title
                                    2 - Release Year
                                    3 - Rating
                                    4 - Duration
                                    5 - Genre
                                    Enter Value: """)
            value_to_change = input(
                "What would you like to update the value to? ")

            cursor.execute(
                f"UPDATE tblFilms SET {field_to_change} = '{value_to_change}' WHERE filmID = {film_id}"
            )
            conn.commit()
            sleep(2)
            amend_again = input(
                "Would You like to amend another Movie? Enter Y or N: ").upper(
                )
            if amend_again == "Y":
                amend_movie()

    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be updated. Check that database and/or table exists: {e}"
        )


if __name__ == '__main__':
    amend_movie()
