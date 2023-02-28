import random


def players(playerName):
    player = playerName
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
    print(f"Player {player} Score : {playerScore}")
    return player, playerScore, dice
    # return dice


argPlayerName1 = input("Enter player name: ")
argPlayerName2 = input("Enter player name: ")

player1 = players(argPlayerName1)
player2 = players(argPlayerName2)
if player1[1] > player2[1]:
    print(f"Player {player1[0]} rolled {player1[1]} and is the winner! ")
else:
    if player1[1] < player2[1]:
        print(f"Player {player2[0]} rolled {player2[1]} and is the winner! ")
    else:
        print(
            f"Its a draw! | Player {player1[0]} rolled {player1[1]} | Player {player2[0]} rolled {player2[1]}"
        )
