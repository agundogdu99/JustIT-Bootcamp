"The for loop can be used to iterate through a string and any sequence of elements(eg numbers etc)"

"To Do: Predict, then Run, and then Investigate"
name = "Abdul is Software Technical Trainer"
for letter in name:
    print(letter, end="")
print("\n")


searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")
print(searchStr[3])
"""The membership operator can be used to check if a value/substring is present
or not in object and returns true if it does"""
if findChar in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f"Not Found {findChar}")

# "Exercise: replace the in operator with the 'not in' operator "

if findChar not in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Not Found {findChar}")
else:
    print(f"Found {findChar}")


# Further reading on operators not covered in the bootcamp see links below
"https://www.w3schools.com/python/gloss_python_identity_operators.asp"
"https://www.w3schools.com/python/gloss_python_bitwise_operators.asp"

"To Do: Task1:"
# You have been provided with the vowels in a list data structure and a variable
# name that is assigned with an empty string.

"Your task is to assign your name to the variable called name and use a for loop and if statement to:"
"Iterate through the list of vowels to find the vowels in your name"
"          0,   1  ,   2,  3,  4"
vowels = ["a", "e", "i", "o", "u", "j"]  # vowels
name = "Jane Smith"  # Add your name in between the speech marks
for char in name:
    if char in vowels:
        print(char, end="")
    else:
        print("No vowels in your name")


print("\n")
