import sys

sys.path.insert(0, "Python/Projects/FilmFlix Project/FilmFlix_Delete")
sys.path.insert(0, "Python/Projects/FilmFlix Project/FilmFlix_Amend")
sys.path.insert(0, "Python/Projects/FilmFlix Project/FilmFlix_Add")
sys.path.insert(0, "Python/Projects/FilmFlix Project/FilmFlix_Print")
sys.path.insert(0, "Python/Projects/FilmFlix Project/FilmFlix_Reports")
sys.path.insert(0, "Python/Projects/FilmFlix Project/FilmFlix_Search")
from FilmFlix_Add.add_movie import *
from FilmFlix_Delete.delete_movie import *
from FilmFlix_Amend.amend_movie import *
from FilmFlix_Print.print_movies import *
from FilmFlix_Reports.generate_report import *
from FilmFlix_Search.search_movie import *

import add_movie
import delete_movie
import amend_movie
import print_movies
import generate_report
import search_movie


def filmflix_menu():
    option = 0
    print("Welcome to Ahmet's Film Flix Database...")
    print("""Please enter one of the following options...
                1 - Add a Movie
                2 - Delete a Movie
                3 - Amend a Movie Record
                4 - Print all Movie Records
                5 - Generate a Report
                6 - To Search
                7 - Exit
          """)
    option = input("Enter Choice: ")
    while option not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Please enter a valid selection from the Menu options")
        option = input("Enter Choice: ")
    return option


main_program = True
while main_program:
    # Execute Main Menu
    flix_menu = filmflix_menu()
    if flix_menu == "1":
        add_movie.add_movie()
    elif flix_menu == "2":
        delete_movie.delete_movie()
    elif flix_menu == "3":
        amend_movie.amend_movie()
    elif flix_menu == "4":
        print_movies.print_movies()
    elif flix_menu == "5":
        generate_report.report_menu()
    elif flix_menu == "6":
        search_movie.search_movie()
    else:
        print("Goodbye...")
        main_program = False

# Iframe on HTML page

# Look at flask
