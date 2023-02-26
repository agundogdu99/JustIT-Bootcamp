searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")

"To Do: Predict, then Run, and then Investigate"
"iterate over a string to find an count a character"

# we set count to the value of zero
counter = 0
# loop through the entire string to search for the character entered
for aChar in searchStr:
    # check if the character entered is a match with any character in the string
    if aChar == findChar:
        # increase the count by 1 every time you find the same character
        counter = counter + 1
print(f"Find the character : {findChar} {counter} times")  # display the result

"To Do: Task1:"
# refactor the code above by putting it into a subroutine and invoke it


def findCharacter(searchChar, string):
    count = 0
    for char in string:
        if char == searchChar:
            counter += 1
    return f"The character {searchChar} appears {count} times in your string '{string}'"


print(findCharacter("a", "The quick brown fox jumps over the lazy dog"))
