"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""


"Predict, then Run, and then Investigate"

userAge = 17  # int(input("Enter your age: "))

ageLimit = 16

passCode = "Bootcamp"

# compare if the value held in userAge is greater than the value held in ageLimit
if userAge >= ageLimit:

    # execute the code bloc below if the comarison returns true
    userCode = input('Enter Usercode')
    if userCode == passCode:
        print('You met the age requirement')
    # nested if will execute if the codition above is true (if userAge > ageLimit:)


"To Do: Q&A"
"What do you think is the equivalent of JS nested if in python?"
# if (condition) {
# if (nested condition) {
# Code Block
# }
# }


"Modify"
"To Do: Task 1: Using if elif and else"
# Exercise: Modify the code above to use else for both the outer if and the nested if condition

if userAge >= ageLimit:
    userCode = input('Enter Usercode')
    if userCode == passCode:
        print('Access granted. Password Correct')
    else:
        print('You have entered an incorrect password!')
else:
    print('You are below the age limit')
