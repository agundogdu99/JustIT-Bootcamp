def findHighestNum(a, b):
    if a > b:
        return a
    else:
        return b


answer = findHighestNum(310, 100)
print(f"The highest number is {answer} ")

answer1 = findHighestNum(3101, 10000)
print(f"The highest number is {answer1} ")

answer2 = findHighestNum(30, 10)
print(f"The highest number is {answer2} ")
