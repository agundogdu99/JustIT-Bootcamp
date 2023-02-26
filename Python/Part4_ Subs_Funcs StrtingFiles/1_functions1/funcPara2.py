"To Do: Predict, then Run, and then Investigate"


def addition():
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")


"Modify"
"To Do: Task1: Modify the code above to use a parameter"


def addition_1(num1, num2):
    return num1 + num2


print(addition_1(5, 10))


# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":
    addition()


"Further reading on python functions"
#
