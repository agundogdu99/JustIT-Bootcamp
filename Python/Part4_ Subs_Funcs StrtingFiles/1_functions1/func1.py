
"As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections"
"In python function is a type of subroutine, asubroutine is sequence of instructions to perform a specific task with an identifiable name."

"A subroutine(function) definition is used to define the steps within the subroutine(function)"

"A subroutine(function) may or may not have a return statement"

"A subroutine(function) may or may not have parameters"

"def just defines the subroutine(function)"

"A subroutine(function) is not executed unless the subroutine is called."

"A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"


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

# "To Do: Predict, then Run, and then Investigate"

# name = "Emjay"
# print("Your name is: ", name)

# name = input(("What is your name? "))
# print("Your name is: ", name)

# def define the subroutine/function user


def user():
    name = "Emjay"
    address = "111 Python Street"
    interest = "swimming"
    print(f"Your name is: {name}, of {address} and interested in {interest}")


def userName():
    name = input(("What is your name? "))
    print("Your name is: ", name)
    return name


def userName2():
    name = input(("What is your name? "))
    address = input(("What is your address? "))
    interest = input(("What is your interest? "))
    print("Your name is: ", name)
    return name, address, interest


print(f"Welcome {userName2()}")

# def define the subroutine userName

# print("Welcome")
# userName()


"To Do: Task 1: Call the subroutine inside a print function with or without f-strings and explain your result"

print(f"Welcome {userName()}")

"Modify/Make"
"To Do: Task 2: Modify the subroutine to ask for address and interest "
user()  # calls function for the print
print(f"Welcome ")

"Investigate"  # if __name__ == "__main__":
"To Do: Task 3: Copy and paste the code block below in the broswer to investigate it use"
# if __name__ == "__main__":
# Add comment to explain why it can be used in your program in your own words"

# used to check whether a Python file is being run as the main program or if it's being imported as a module into another program


# call/invoke the subroutine
# call/invoke the subroutine


"Knowledge Check"
"Task 4: Linking existing knowledge with new knowldge "
# What do you think is the equivalent of the python 'def' keyword in JavaScript
# function functionName(param) {

# }


"Further reading on python functions"
#
