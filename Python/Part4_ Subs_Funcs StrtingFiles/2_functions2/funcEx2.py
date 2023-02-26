
"To Do: Predict, then Run, and then Investigate"

"To Do: Task1: Add comments to the code to explain what the while loop is doing"
"Further reading on python functions statements"


"""Exercises: Modify the code in subroutine to convert it to a function thats uses
parameter and argument"""


def userName(name, address, interest):  # define the subroutine userName
    # name = input(("What is your name? "))
    return f"Your name is: {name}, address is {address} and interest is {interest}"


print(userName("Ahmet"))

"Extension "


def addition():  # define the addition function
    # variables inside a  surbroutine/function have local scope
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 + num2
    return answer  # returns the value held in the answer variable
