import random

diceList = []


def players():
    player = input("Enter player name: ")
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


rolling = True

while rolling == True:
    player1 = players()
    player2 = players()

    if player1[1] > player2[1]:
        print(f"Player {player1[0]} rolled {player1[1]} and is the winner! ")
    else:
        if player1[1] < player2[1]:
            print(f"Player {player2[0]} rolled {player2[1]} and is the winner! ")
        else:
            print(
                f"Its a draw! | Player {player1[0]} rolled {player1[1]} | Player {player2[0]} rolled {player2[1]}"
            )
            # Similarly, tuples don't have .append and .extend methods as list does. Using += is possible,
            # but it changes the binding of the variable, and not the tuple itself:
    diceList.append(
        f"Player {player1[0]} rolled {player1[1]} Player {player2[0]} rolled {player2[1]} |"
    )
    # diceList.append(f"{player1}  {player2}")
    keepRolling = input("Woull you like to play again? Y/N ").upper()
    if keepRolling == "N":
        break

with open("Review/DiceRoll/Scores.txt", "a") as file1:
    "Method 1"
    savePlay = file1.write(f"\n{diceList}")

    "Method 2"
    # diceRecords = str(diceList)
    # savePlay = file1.write(f"\n{diceRecords}")


# fp1 = str(player1)
# fp2 = str(player2)
# fp1 = player1
# fp2 = player2
with open("Review/DiceRoll/Scores1.txt", "a") as file2:
    savePlay = file2.write(f"\n{player1[0], player1[1]}\n{player2[0], player2[1]}")

print("\n Test")
for dicePlayer in diceList:
    print(dicePlayer)


print("\n Test")
# for aPlayer, bPlayer in zip(player1[:], player2[:]):
#     print(aPlayer, bPlayer)

for aPlayer, bPlayer in enumerate(diceList):
    print(
        f"This is Game {aPlayer +1} |Player {bPlayer[2]} rolled {bPlayer[6:8]} and Player {bPlayer[17]} rolled {bPlayer[21:23]}"
    )  # {player1[0]} rolled {player1[1]}
    # print(aPlayer, bPlayer)
    # for (
    #     iPos,
    #     anItem,
    # ) in enumerate(bPlayer):
    #     print(
    #         f"This is Game {aPlayer +1}, index position {iPos} and item/element value {anItem}"
    #     )
