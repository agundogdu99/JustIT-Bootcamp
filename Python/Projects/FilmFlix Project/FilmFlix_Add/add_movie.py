from connect_flix import *
from time import sleep


def add_movie():
    parameters = []

    title = input("Enter Title Name:  ")
    yearReleased = input("What year was the movie released? - ")
    rating = input("Enter Movie Rating i.e. PG / R etc - ")
    duration = input("What is the Duration of the Movie? - ")
    genre = input("What is the Movie Genre? - ")

    parameters.append(title)
    parameters.append(yearReleased)
    parameters.append(rating)
    parameters.append(duration)
    parameters.append(genre)

    try:
        cursor.execute("INSERT INTO tblFilms VALUES (NULL, ?, ?, ?, ?, ?)",
                       parameters)
        conn.commit()
        print(f"{title} added in the Movie Database")
        sleep(2)
        # Ask User if they want to add another movie into the database
        add_again = input(
            "Would You like to add another Movie? Enter Y or N: ").upper()
        if add_again == "Y":
            add_movie()
    except sql.OperationalError as e:
        print(f"Error, Record not inserted: {e}")


if __name__ == "__main__":
    add_movie()