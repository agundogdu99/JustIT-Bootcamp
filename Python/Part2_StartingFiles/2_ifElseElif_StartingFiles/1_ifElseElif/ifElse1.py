# Selection is used to control the flow of the program

pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"
"Predict, then Run, and then Investigate"
# check the condition that pStudy value is same as the value held in curProgram
if pStudy == curProgram:

    # do something/execute the line of code below if the condition is checked above true
    print('The values are the same')
# The block(else) of code will be executed if the codition in the if block is not met
else:
    print('They are not the same')

"Modify"
"To Do: Exercise"
# Modify the code above to use the "!=" operator, or the "not" operator

if pStudy != curProgram:
    print('They are not the same')
else:
    print('The values are the same')

# Solution 2
if not (pStudy == curProgram):
    print('They are not the same')
else:
    print('The values are the same')
