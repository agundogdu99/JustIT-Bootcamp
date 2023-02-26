
import random
"Make"
"To Do: Task 1: Create a dice rolling python application. The application should:"
# - Generate first random number between 1 and 6 and assign this to a variable
# - Generate second random number between 1 and 6 and assign this to a variable
# - Display the value of rolled dice


dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(
    f"Dice 1 is: {dice1} & Dice 2 is: {dice2}. The total of your dice throw is {dice1 + dice2}")

"To Do: Task 2: Add notes below to explain the application in your own words"

# dice1 gets a random number between 1 and 6 using the randint function of the random module
# dice 2 does the same as above
# A print statement displays the value of dice1 and and dice 2, and also the accumulated value of both
