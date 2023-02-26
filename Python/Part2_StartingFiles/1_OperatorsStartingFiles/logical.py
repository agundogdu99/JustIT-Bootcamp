"Read through the Logical operators examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
# https://www.w3schools.com/python/gloss_python_comparison_operators.asp

"Logical expression evaluates to True or False"
# Logical operators: and , or, not

# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to
# >= 	greater than or equal to
# !=    Not equal to

num1 = 10  # static object/value
num2 = 5  # static object/value
num3 = 11  # static object/value
num4 = 2  # static object/value
# comparison operator
print(num1 == num2)
print(num1 == 10)
print(num2 == 5)


"Predict, then Run, then Investigate, and then Modify"

# Logical operator: and
print("\nLogical operator: and ")
print(num1 == 10 and num2 == 5)
print(num1 == 10 and num2 == 50)
print(num1 == 15 and num2 == 5)

"Modify "
"To Do: Task 1: modify print statemtents to use or operator instead of and"
# Logical operator: or
print("\nLogical operator: or ")
print(num1 == 10 or num2 == 50)
print(num1 == 15 or num2 == 5)


# Logical operator: not
print("\nLogical operator: not ")
print(not (num1 == 10))

"Modify "
"To Do: Task 2: modify print statemtents to use or operator with not"
"Exercise modify print statemtents to use and operator with not"
# Logical operator: not with or
print(num1 != 10 or num2 != 50)
print(num1 != 15 or num2 != 5)
# Solution 2
print(not (num1 == 10 or num2 == 50))
print(not (num1 == 15 or num2 == 5))


"Modify "
"To Do: Task 2: modify print statemtents to use and operator with not"
# Logical operator: not with and
print(num1 != 10 and num2 != 50)
print(num1 != 15 and num2 != 5)
# Solution 2
print(not (num1 == 10 and num2 == 50))
print(not (num1 == 15 and num2 == 5))
