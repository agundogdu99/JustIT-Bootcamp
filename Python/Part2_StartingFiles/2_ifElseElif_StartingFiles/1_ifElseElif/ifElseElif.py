# Selection is used to control the flow of the program

score = int(input("Enter a number: "))
"Predict, then Run, and then Investigate"

# check the condition that score is greater than 100
if score > 100:
    # create avariable and assign it the value Invalid Entry
    grade = 'Invalid Entry'
# check the condition that score is between 75 and 100
if score >= 75 and score <= 100:
    # create avariable and assign it the value A
    grade = 'A'
# check the condition that score is between 60 and 74
elif score > 60 and score <= 74:
    # reassign the grade variable the value B
    grade = 'B'
# check the condition that score is between 50 and 59
elif score >= 50 and score <= 59:
    # reassign the grade variable the value C
    grade = 'C'
# reassign the grade variable the value F
else:
    grade = 'F'

"To Do: Q&A"
"What do you think is the equivalent of JS else if in python?"
# if (condition) {
# code
# } else if (condition) {
# code
# } else {
# code
# }


"Make"
"To Do: Task 1: Using if elif and else"
# Create a Menu program that allow user to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice

subj1 = input(
    'Enter 1 for Maths. 2 for Science. 3 for Music - OR enter Q to exit')
if subj1 == "1":
    print('You chose Maths')
elif subj1 == "2":
    print('You chose Science')
elif subj1 == "3":
    print('You chose Music')
elif subj1 == "Q":
    print('You have exited the program')
else:
    print('You entered an invalid selection')


"To Do: Task 2:"
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]

for i in numList:
    if i == 78:
        print(f'I just found {i}!')
        continue
    elif i == 88:
        print(f'I just found {i} as well!')
        continue
    else:
        print(f'I couldnt find any of the values in index {numList.index(i)}')
