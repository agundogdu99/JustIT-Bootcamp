from addDownloads import *
from readDownloads import *
from updateDownloads import *
from deleteDownloads import *
from searchDownloads import *

# Create a menu using a function


def downloadsMenuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", "6"]:
        print(
            "Downloads Menu Options\n1. To Read\n2. To Add\n3. To Update\n4. To Delete\n5. To Search\n 6. To Exit"
        )

        options = input("Enter an option from the menu choices above: ")

        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice")
        return options


def dbDownloads():
    mainProgram = True
    while mainProgram:
        downloadsMenu = downloadsMenuOptions()
        if downloadsMenu == "1":
            print("Welcome to Read Downloads")
            read()
        elif downloadsMenu == "2":
            insertDownloads()
        elif downloadsMenu == "3":
            print("Welcome to Update")
            update()
        elif downloadsMenu == "4":
            print("Welcome to Delete")
            delete()
        elif downloadsMenu == "5":
            print("Welcome to Search")
            search()
        else:
            print("Exiting the Downloads menu")
            mainProgram = False
        # return mainProgram


if __name__ == "__main__":
    dbDownloads()