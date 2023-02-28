import random

lottoNums = []


def generateRandomNums():
    nums = random.randint(1, 49)

    ##luckyN = int(luckyN)
    return nums


for counter in range(0, 7):
    # print(generateRandomNums())
    lottoNums.append(generateRandomNums())
print(lottoNums)
