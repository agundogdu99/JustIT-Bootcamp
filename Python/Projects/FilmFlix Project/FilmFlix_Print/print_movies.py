from connect_flix import *


def print_movies():
    try:
        cursor.execute("SELECT * FROM tblFilms")
        rows = cursor.fetchall()
        if rows == None:
            print("Error. Cannot Read Database")
        else:
            for row in rows:
                print(row)
    except sql.OperationalError as e:
        print(f"Error, Record cannot be read: {e}")


if __name__ == "__main__":
    print_movies()
