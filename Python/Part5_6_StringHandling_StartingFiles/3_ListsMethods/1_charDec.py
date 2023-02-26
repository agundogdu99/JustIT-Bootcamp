"Use chr() and ord() to peform ASCII conversion"
# Perform ASCII conversion in pyhon
# chr(97): takes in a decimal number and returns its character equivalent
# ord("a"): takes in a character and returns its character decimal equivalent

"To Do: Predict, then Run, and then Investigate"
aChar = input("Enter a character: ")
# ord("a"): takes in a character: Return the Unicode code point for a one-character string.
convertChar = ord(aChar)  # ord"(a/b/c/d")
print(convertChar)

"To Do: Task2: Modify the code above to ask for an integer value then use the chr() to return its character equivalent"
"solution"
anInt = int(input("Enter a number: "))
convertInt = chr(anInt)
print(convertInt)

"""To Do: Task2: Complete the code block below to print a list of converted numbers as letter
 The question marks indicates where the code is missing  
"""
"Uncomment the code to complete th task"


def alphabets():  # created the function alphabets
    alphabetList = []  # create an empty list
    for letters in range(65, 123):
        # converts numbers to letters then add/append them to
        alphabetList.append(chr(letters))
    return alphabetList


print(alphabets())
