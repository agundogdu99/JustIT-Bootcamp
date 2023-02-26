cardValue = "Kings"
suitOfCards = "Hearts"

"Predict, then Run, and then Investigate"
chkCardValue = input("Enter card value: ").title()

chkCardSuit = input("Enter card suit: ").title()


if cardValue == chkCardValue and suitOfCards == chkCardSuit:
    print("Winner!")
else:
    print("Try Again")


"Modify"
"To Do: Exercise"
# Modify the code above to use the "or" operator, or the "not" operator with the and operator

# Solution 1
if not (cardValue == chkCardValue and suitOfCards == chkCardSuit):
    print("Try Again")
else:
    print("Winner!")

# Solution 2
if cardValue != chkCardValue and suitOfCards != chkCardSuit:
    print("Try Again")
else:
    print("Winner!")
