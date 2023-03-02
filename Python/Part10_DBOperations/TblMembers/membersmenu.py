from addMembers import *
from readMembers import *


# Create a menu using a function

# Main Songs Menu

def membersMenuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", "6"]:  # , "4"]:
        print("Members Menu Options\n1. To Read\n2. To Add\n3. To Update\n4. To Delete\n5. To Search\n 6. To Exit")

        options = input("Enter an option from the menu choices above: ")

        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice")
        return options


# print(songsMenuOptions())


mainProgram = True
while mainProgram:
    membersMenu = membersMenuOptions()
    if membersMenu == "1":
        print("Welcome to Read Songs")
    elif membersMenu == "2":
        insertMembers()
    elif membersMenu == "3":
        print("Welcome to Update")
    elif membersMenu == "4":
        print("Welcome to Delete")
    elif membersMenu == "5":
        print("Welcome to Search")
    else:
        print("Exiting the songs menu")
        mainProgram = False
