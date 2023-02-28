def strEcho(inWord):
    for aLetter in inWord:
        print(aLetter * 8)


myString = input("Please enter a message >> ")
strEcho(myString)
