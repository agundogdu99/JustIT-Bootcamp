# Syntax
"""
def subroutine/functionName():
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)

#call/invoke the subroutine/function
subroutineName/function()
"""
"A subroutine(function) may or may not have a return statement"
"A subroutine(function) may or may not have parameters"


"To Do: Predict, then Run, and then Investigate"


def user():  # define the subroutine/function userName
    name = "Emjay"
    print("Your name is: ", name)


def userName():  # define the subroutine userName
    name = input(("What is your name? "))
    print("Your name is: ", name)


# call/invoke the functioneName
# "Method 1"
def addition():  # defines the addition function
    # variables inside a  surbroutine/function have local scope
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 + num2
    return answer


print(addition())
print(f"Method 2\nThe answer is {addition()}")

# "Method 2"
# # Assigned the function to the variable myAddition
myAddition = addition()

print(f"Method 2\nThe answer is {myAddition}")


# What is the difference between a function in JS and a function in python ?

def addition():  # defines the addition function
    # variables inside a  surbroutine/function have local scope
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 + num2


"Exercise: modify the code in userName subroutine  to convert it to a function "


def userName():  # define the subroutine userName
    name = input(("What is your name? "))
    return f"Your name is: {name}"
