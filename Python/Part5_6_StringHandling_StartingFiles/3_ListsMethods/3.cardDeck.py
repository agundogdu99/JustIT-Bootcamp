# https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
# ♥ ♦ ♣ ♠
from random import shuffle, choice

suits = ["♥", "♦ ", "♣", "♠"]
deck = []

for aSuit in suits:
    # print(aSuit)
    # loop thrugh from number 1 .....13
    for aCard in range(1, 14):  # nested for loop
        if aCard == 11:
            # change/replace the value from 11 to J and add it to the empty list called deck
            deck.append("J" + aSuit)
        elif aCard == 12:
            # change/replace the value from 12 to Q and add it to the empty list called deck
            deck.append("Q" + aSuit)

        elif aCard == 13:
            # change/replace the value from 13 to K and add it to the empty list called deck
            deck.append("K" + aSuit)

        elif aCard == 1:
            # change/replace the value from 1 to A and add it to the empty list called deck
            deck.append("A" + aSuit)
        else:
            deck.append(str(aCard) + aSuit)

print(f"This card Deck has a total of {len(deck)} cards")
print(f"{deck}\n")
shuffle(deck)
print(f"The shuffled Deck{deck}\n")

# players
player1Deck = deck[0:26]
player2Deck = deck[26:52]


print(f"Player1 Deck\n {player1Deck}\n")
print(f"Player1 Deck\n {player2Deck}\n")


p1choice = choice(player1Deck)
print(p1choice)
p2choice = choice(player2Deck)
print(p2choice)

if p1choice[0] == p2choice[0]:
    print(f"Its a tie Player1 card: {p1choice} | Player2 card: {p2choice}")
elif p1choice[0] > p2choice[0]:
    print(f"Player1 card: {p1choice} wins! | Player2 card: {p2choice} lose")
else:
    if p2choice[0] > p1choice[0]:
        print(f"Player2 card: {p2choice} wins! | Player1 card: {p1choice} lose")
p1Deck = []
p2Deck = []

p1Deck.append(p1choice[0])
p2Deck.append(p2choice[0])

print(p1Deck)
print(p2Deck)
