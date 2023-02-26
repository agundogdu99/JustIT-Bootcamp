"""You can perform operations with string in a similar way to the operations 
that you can perform with numbers. """

"To Do: Predict, then Run, and then Investigate"

stringVal1 = "a" > "b"  # check if the letter a is greater than b
print(stringVal1)


stringVal2 = "b" > "a"  # check if the letter b is greater than a
print(stringVal2)

"You can multiply a string, it will concatenate the same value for the number of times stated."
mutiplyWord = "Python\n" * 5  # mulitply the word n times
print(mutiplyWord)

"""The + sign concatenates (joins) the two string together.
There is no space because it hasn't been given that instruction"""
joinWords = "Python" + " " + "Java"  # join the two words
print(joinWords)

"Exercise"
# Create two variables fName and lName and join and print them using a variable called fullName
fName = "Ahmet"
lName = "Gundogdu"
fullName = f"{fName} {lName}"


"What is the len() used for in a string?"
# To obtain the length of the string i.e. how mancy characters
course = "Python"
wordLength = len(course)
print(wordLength)

"How can we print a specific character using the index value or position in a string or list?"
findChar = course[3]
print(findChar)

"Exercise: Write the code to print the letter  h"
"Exercises"
#  Return all the characters from the string held in the course variable using negative values
print(course[-1], course[-2], course[-3], course[-4], course[-5], course[-6])

# Solution 2
for i in range(len(course)-1, -1, -1):
    print(course[i], end="")
print("\n")

#  use any comparison operator to compare the letter "a" and "A"
compareA = "a" < "A"

#  use any comparison operator to compare the letters "ax" and "ZZ"
compareZZ = "ax" > "ZZ"

#  use any comparison operator to compare your firstname with any another first name
nameCompare = "Ahmet" != "Hulk"

# != , == , <= , >=, <,>


course = "Python Programming"
wordLength = len(course)
print(f"The length of the string {course} is {wordLength}")
