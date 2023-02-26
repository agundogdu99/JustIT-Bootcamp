
"To Do: Predict, then Run, and then Investigate"


# num1 = int(input(("Enter your first number: ")))
# num2 = int(input(("Enter your second number: ")))
# answer = num1 + num2
# print(f"The answer to {num1} + {num2} = {answer}")
# print(
#     "Executing...some code and processes....\nExecuting...some code and processes....\n......"
# )


"To Do: Task 1: Data Types: Value Error"
# In the terminal Enter a numeric values to perform addition and take note of the output()
# In the terminal Enter a numeric value and string value(ten/one/two) to perform addition and take note of the output()


try:
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 + num2
except ValueError:
    # An exception is a runtime error which will cause issues or render your app unusable for you and other users if not handled
    print(f"Please enter a numeric value")
else:  # Else block always executes... provided try block is a success
    print(f"The answer to {num1} + {num2} = {answer}")
finally:  # Will execute regardless of the above being valid or not
    print('Closing Application')
    # https://www.w3schools.com/python/python_ref_exceptions.asp
    # https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception
