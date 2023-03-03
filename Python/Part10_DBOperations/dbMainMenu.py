import sys

sys.path.insert(0, "Python/Part10_DBOperations/TblSongs")
sys.path.insert(0, "Python/Part10_DBOperations/TblMembers")
sys.path.insert(0, "Python/Part10_DBOperations/TblDownloads")
import songsmenu
import membersmenu


def dbMenuOptions():
    options = 0
    while options not in ["1", "2", "3", "4"]:
        print(
            "Main Menu Options\n1. Songs\n2. Members\n3. Downloads\n4. To Exit\n"
        )

        options = input("Enter an option from the menu choices above: ")

        if options not in ["1", "2", "3", "4"]:
            print(f"{options} is not a valid choice")
        return options


# print(songsMenuOptions())

mainProgram = True
while mainProgram:
    dbMenu = dbMenuOptions()
    if dbMenu == "1":
        songsmenu.dbSongs()
    elif dbMenu == "2":
        membersmenu.dbMembers()
    elif dbMenu == "3":
        print("Welcome to downloads")
    else:
        print("Exiting the songs menu")
        mainProgram = False
print("Press a key to exit...")