"Use the link provided below to investigate Tenary Operators in python"
# https://www.w3docs.com/snippets/python/how-to-write-inline-if-statement-for-print.html

"Make"
"To Do: Use any two of your existing 'if else' and or 'if,elif and else' programs"
# 1. Create/modify existing program using the Tenary Operators syntax
print('Access granted. Password Correct') if userAge >= ageLimit and userCode == passCode else print(
    'You have entered an incorrect password!') if userAge >= ageLimit else print('You are below the age limit')
# 2. From your investigation and implementation of Tenary Operators program explain:
# -(a) any use case for using or not using Tenary Operators
"It can make code easier to write on a single line, and easy to read if its short"
# -(b) any limitiation(s) for using or not Tenary Operators
"It can make code hard to read in more complex situations like the above. It can be too long as well"

# Example 2
print('Logged in') if userPassword == userStoredPassword else print('Not logged in')
"In this example, it is easy to read and concise as it is short and to the point..."
