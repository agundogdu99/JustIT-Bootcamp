from addSongs import *
from readSongs import *
from updateSongs import *
from deleteSongs import *
from searchSongs import *

# Create a menu using a function

# Main Songs Menu


def songsMenuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", "6"]:  # , "4"]:
        print(
            "Songs Menu Options\n1. To Read\n2. To Add\n3. To Update\n4. To Delete\n5. To Search\n 6. To Exit"
        )

        options = input("Enter an option from the menu choices above: ")

        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice")
        return options


# print(songsMenuOptions())


def dbSongs():

    mainProgram = True
    while mainProgram:
        songsMenu = songsMenuOptions()
        if songsMenu == "1":
            print("Welcome to Read Songs")
            read()
        elif songsMenu == "2":
            insertSongs()
        elif songsMenu == "3":
            print("Welcome to Update")
            update()
        elif songsMenu == "4":
            print("Welcome to Delete")
            delete()
        elif songsMenu == "5":
            print("Welcome to Search")
            search()
        else:
            print("Exiting the songs menu")
            mainProgram = False
        # return mainProgram


if __name__ == "__main__":
    dbSongs()