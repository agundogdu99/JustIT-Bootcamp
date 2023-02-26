from random import shuffle, choice


def create_deck(suits):
    deck = []
    for aSuit in suits:
        for aCard in range(1, 14):
            if aCard == 1:
                card_value = "A"
            elif aCard > 1 and aCard < 11:
                card_value = str(aCard)
            elif aCard == 11:
                card_value = "J"
            elif aCard == 12:
                card_value = "Q"
            elif aCard == 13:
                card_value = "K"
            deck.append(card_value + aSuit)
    return deck


def play_game(deck):
    shuffle(deck)
    player1Deck = deck[0:26]
    player2Deck = deck[26:52]
    print(f"Player1 Deck\n{player1Deck}\n")
    print(f"Player2 Deck\n{player2Deck}\n")

    p1choice = choice(player1Deck)
    p2choice = choice(player2Deck)
    print(p1choice)
    print(p2choice)

    if p1choice[0] == p2choice[0]:
        print(f"It's a tie! Player1 card: {p1choice} | Player2 card: {p2choice}")
    elif p1choice[0] > p2choice[0]:
        print(f"Player1 card: {p1choice} wins! | Player2 card: {p2choice} loses")
    else:
        print(f"Player2 card: {p2choice} wins! | Player1 card: {p1choice} loses")

    p1Deck = []
    p2Deck = []

    p1Deck.append(p1choice[0])
    p2Deck.append(p2choice[0])

    print(p1Deck)
    print(p2Deck)

    p1Deck1 = []
    p2Deck1 = []

    p1Deck1.append(p1choice)
    p2Deck1.append(p2choice)
    print(p1Deck1)
    print(p2Deck1)

    p1Deck1.append(len(p1choice))
    p2Deck1.append(len(p2choice))
    print(p1Deck1)
    print(p2Deck1)


suits = ["♥", "♦", "♣", "♠"]
deck = create_deck(suits)
play_game(deck)
