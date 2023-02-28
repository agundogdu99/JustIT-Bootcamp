import random


def players():
    playerName = input("Enter player name: ")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2}")
    dice = die1 + die2  # value from both dice
    if dice == 12:
        dice = 0  # re-assign the value of dice to 0
        print("Disqualified")
    else:
        if die1 == die2:
            dice = dice * 2
    playerScore = dice
    print(f"Player {playerName} Score : {playerScore}")
    # players  0         1         2
    return playerName, playerScore, dice
    # return dice


player1 = players()  # call player 1
player2 = players()  # call player 2
if player1[1] > player2[1]:  # player1 score is greater than player2 score
    print(f"Player {player1[0]} rolled {player1[1]} and is the winner! ")
else:
    if player1[1] < player2[1]:  # player1 score is lesser than player2 score
        print(f"Player {player2[0]} rolled {player2[1]} and is the winner! ")
    else:  # player1 score is equals to player2 score
        print(
            f"Its a draw! | Player {player1[0]} rolled {player1[1]} | Player {player2[0]} rolled {player2[1]}"
        )
