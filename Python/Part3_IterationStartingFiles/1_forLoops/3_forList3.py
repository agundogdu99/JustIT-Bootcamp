"""
Break in Python Python break is generally used to terminate a loop. 
This means whenever the interpreter encounters the break keyword, 
it simply exits out of the loop. Once it breaks out of the loop, 
the control shifts to the immediate next statement.
"""


"To Do: Predict, then Run, and then Investigate"

# Combining iteration and Selection"

numList = [1, 3, 4, 6, 1, 3, 5, 7]
for number in numList:
    if (number == 30):
        print("found", number)
        break
else:
    print("Number not found")


"Modify/Make"
"To Do: Task 1: You have been provided with a list of modules below, write a for loop similar to the one above to break out of the loop when 'Python' is found"
# Refer to the code above to gide you in completing this task

course_list = ['html', 'css', 'sql', 'python', 'javascript']

for course in course_list:
    if course == 'python':
        print('Just found Python!')
        break
    else:
        print('Couldnt find it :(')
