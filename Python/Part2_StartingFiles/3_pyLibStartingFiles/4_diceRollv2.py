import random

"Modify "
"To Do: Task 1: You have been provided with an incomplete diceRoll.py program with bugs to debug and fix"

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(f"Dice: {dice1} | Dice: {dice2}")

dice = dice1 + dice2  # What i the values of both dice

if dice == 12:  # check if both dice equals 12
    dice = dice * 2  # double the total from both dice
    print(
        f"You threw {dice1} and {dice2}, but because they = {dice}, you get a double multiplier bonus!")
elif dice1 == dice2:
    # dice = dice  # 10 = 10
    print(
        f"You threw a total of {dice}. Wow! Both of your dices were the same!")
else:
    print(
        f"You threw a total of {dice}, and the previous 2 conditions were not met!")


"To Do: Task 2: Add notes below to explain the application in your own words"

# dice1 gets a random number between 1 and 6 using the randint function of the random module
# dice 2 does the same as above
# A print statement displays the value of dice1 and and dice 2

# A conditional statement also checks if the value of both dices (dice variable) is equivelant
#       And if so, if doubles its value and prints it
# Failing the above conditional check, another condition checks to see if dice1 is the same value as dice2.
#       If so, it prints the value to the screen and tells the user that both of their dices were the same value
# Failing above 2 conditions tells the user that their previous 2 conditions were not met, and displays the dice value
