
"To Do: Predict, then Run, and then Investigate"

"To Do: Task1: Add comments to the code to explain what the while loop is doing"
"Further reading on python functions statements"


"Exercise: modify the code in userName subroutine below to convert it to a function "


def userName():  # define a subrouitine called userName
    fullName = input("Enter your name: ")
    address = input("Enter your address: ")
    interest = input("Any interest? ")
    return f"my name is {fullName}, my address is {address} and my interest is {interest}"


print(userName())


############################################

def userName1():
    fullName = "Ahmet"
    address = "London Bridge"
    interest = "Something..."
    return fullName, address, interest  # returning a tuple of three values


# unpacking the tuple into separate variables
name, address, interest = userName1()
print(name)
print(address)
print(interest)
