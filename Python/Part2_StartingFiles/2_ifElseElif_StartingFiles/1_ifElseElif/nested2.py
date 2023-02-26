"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""


"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""


"To Do: Predict, then Run, and then Investigate and then comment the code to explain each line of code does"

pyCourse = float(input("Enter your python score: "))
htmlCourse = float(input("Enter your HTML score: "))
# float is Explicitly Casted by User
sqlCourse = float(input("Enter your SQL score: "))

"To Do: Explain what is casting and comment on the line of code where casting is used?"
if pyCourse < 45:
    # Text inside "" are explicitly casted as string by user
    print(f"Try again in python {pyCourse}")
elif htmlCourse < 45:                        # 45 is implicitly casted as INT by Python
    # htmlCourse is implicitly casted due to our explicit casting at the INPUT stage
    print(f"Try again in HTML {htmlCourse}")
elif sqlCourse < 45:
    print(f"Try again in SQL {sqlCourse}")


else:
    gradesAverage = (pyCourse + htmlCourse + sqlCourse) / 3
    if gradesAverage <= 55:
        print(f" Your score is {gradesAverage} and is Grade C ")
    if gradesAverage <= 79:
        print(f" Your score is {gradesAverage} and is Grade B")
    if gradesAverage <= 89:
        print(f" Your score is {gradesAverage} and is Grade B ")
