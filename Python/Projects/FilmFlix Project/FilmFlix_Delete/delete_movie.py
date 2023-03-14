from connect_flix import *
from time import sleep


def delete_movie():

    try:
        film_id = input(
            "Which Movie do you want to delete? Plesae select by Movie ID... ")

        cursor.execute(f"SELECT * FROM tblFilms where filmID = {film_id}")
        row = cursor.fetchone()

        if row == None:
            print(f"No record with the Film ID {film_id}")
        else:

            # Method 1
            cursor.execute(f"DELETE FROM tblFilms where filmID = {film_id}")
            # Method 2
            # cursor.execute("DELETE * FROM songs where songID =" + film_id)
            conn.commit()

            sleep(2)
            delete_again = input(
                "Would You like to add another Movie? Enter Y or N: ").upper()
            if delete_again == "Y":
                delete_movie()

    except sql.OperationalError as e:
        print(
            f"Error, Record cannot be deleted. Check that database and/or table exists: {e}"
        )


if __name__ == "__main__":
    delete_movie()
