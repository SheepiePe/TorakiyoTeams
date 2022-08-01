#13195 の素因数は 5, 7, 13, 29 である.
#600851475143 の素因数のうち最大のものを求めよ.

def main():
    resultNum = 600851475143
    countFactor = 2
    while resultNum > 1:
        if resultNum % countFactor == 0:
            resultNum = int(resultNum / countFactor)
            print(resultNum)
            countFactor = 1
        if checkNum(resultNum):
            break

        countFactor = countFactor + 1
    print(resultNum)


def checkNum(targeNum):
    for i in range(2, int(targeNum**0.5) + 1):
        if targeNum % i ==0:
            return False
    return True



main()