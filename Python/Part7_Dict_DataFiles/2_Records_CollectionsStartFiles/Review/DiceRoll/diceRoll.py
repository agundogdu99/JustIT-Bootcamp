from random import randint

"Player 1"
# variable = randintMethod (start value, end value)
die1 = randint(1, 6)
die2 = randint(1, 6)
print(f"Die1: {die1} | Die2: {die2} ")
dice = die1 + die2  # add the values from die1 and die2
if dice == 12:  # execute the code below if die1 and die2 adds up to 12
    print(dice)
    dice = 0  # re-assign the value of dice from 12 to 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player1Score = dice
print(f"Player 1 score: {player1Score} ")
# Exercise copy the code above and modify for player2
"Player 2"
# variable = method (start value, end value)
die1 = randint(1, 6)
die2 = randint(1, 6)
print(f"Die1: {die1} | Die2: {die2} ")
dice = die1 + die2  # add the values from die1 and die2
if dice == 12:  # xecute the code below if die1 and die2 adds up to 12
    print(dice)
    dice = 0  # re-assign the value of dice from 12 to 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player2Score = dice
print(f"Player 2 score: {player2Score} ")
# check /compare values held in player1score with player2score to find a winner
if player1Score > player2Score:
    print(f"Player 1 rolled {player1Score} and is the winner ")
else:
    if player1Score < player2Score:
        print(f"Player 2 rolled {player2Score} and is the winner ")
    else:
        print(
            f" Its a draw | Player 1 rolled {player1Score} | Player 2 rolled {player2Score} "
        )
