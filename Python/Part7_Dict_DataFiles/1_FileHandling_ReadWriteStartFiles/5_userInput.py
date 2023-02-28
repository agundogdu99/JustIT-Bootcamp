fname = input("Enter you full name: ")
address = input("Enter your address: ")
interest = input("Enter your interest: ")
age = int(input("Enter your age: "))

"Make"
"To Do: Task 1: use the code above to ask for user input and then save it to a file called userDetails.txt"

with open(
        "Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/userinput.txt", "a") as details:
    details.write(
        f"Name: {fname}\nAddress: {address}\nInterest: {interest}\nAge: {age}")


"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp
