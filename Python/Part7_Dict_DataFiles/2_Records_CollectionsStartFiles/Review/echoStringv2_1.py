def strEcho(inWord, sizeofEcho):
    for aLetter in inWord:
        print(aLetter * sizeofEcho)


myString = input("Please enter a message >> ")
noofTimes = int(input("Please enter number of times"))
strEcho(myString, noofTimes)
