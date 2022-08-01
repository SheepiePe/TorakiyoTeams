"""
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
"""


def main():
    numberMax = 999
    numberMin = 100
    maxPalindrome = 0

    for i in range(numberMin, numberMax + 1, 1):
        for j in range(numberMin, numberMax + 1, 1):
            targeNum = i * j
            if len(str(targeNum)) < 6:
                continue
            if checkPalindrome(targeNum):
                if maxPalindrome < targeNum:
                    maxPalindrome = targeNum
                break

    print(maxPalindrome)



def checkPalindrome(targeNumber):
    numbersList = list(str(targeNumber))
    if numbersList[0] == numbersList[5] and numbersList[1] == numbersList[4] and numbersList[2] == numbersList[3]:
        return True
    else:
        return False

main()