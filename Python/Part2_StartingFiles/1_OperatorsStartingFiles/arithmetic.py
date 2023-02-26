"Arithmetic  expression evaluates to a number"

num1 = 10  # static object/value
num2 = 5  # static object/value
num3 = 11  # static object/value
num4 = 2  # static object/value

# + operator is use for adddition and also concatenation(join things)

print("Addition: " + str(num1) + " + " + str(num2) + "=", num1 + num2)

# Using f-strings to format print statement (f followed by quotes)
# strings cater for all data types

# plus operator +
print(f"Using f-strings\nAddition: {num1} + {num2} = { num1 + num2} ")

"To Do: Task 1: What is the equivalent of f-strings in JavaScript?"
# Object Literal? `Backticks ${value}`

"""Exercise: write the code to perform the arithmetic operations below using num3 and num4 variables . 
Format your print statement with f-strings"""
print(f"The value of {num3} + {num4} is: {num3 + num4}")

"Modify "
"To Do: Task 2: You have been provided with incomplete code to debug and fix"
"""
write the code to perform the arithmetic operations below using num3 and num4 variables . 
Format your print statement with f-strings
"""

# division /
"use num3 and num4 variables"
print(f"Division (/): {num3} / {num4} = {num3 / num4}")

# Floor division //
"use num3 and num4 variables"
print(f"Floor division (//):{num3} // {num4} = {num3 // num4}")

# Modulus %
"use num3 and num4 variables"
print(f"Modulus (%): {num3} % {num4} = {num3 % num4}")


"To Do: Knowledge check: Explain the operators listed below "
# Division (/) # Simple division, returns a float
# Floor Division (//) # SImple division, but returns the INT value. by removing anything after the decimal
# Modulus (%) # Returns the remainder value of the division
"To Do: Explain when you would use the oprators listed above"
# Division. When exact value is required
# When you require an INT value to be returned and do not need the remainder
# You can check if a number is even or not. Or to simply check if a number goes into another number without remainder
