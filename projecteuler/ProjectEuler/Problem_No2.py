"""
フィボナッチ数列の項は前の2つの項の和である. 
最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
数列の項の値が400万以下のとき, 値が偶数の項の総和を求めよ.
"""

def main():
    count = 2
    numList = [1,2]
    reslutNum = 2
    while count > 1:
        sumNum = numList[count - 2] + numList[count - 1]
        if sumNum > 4000000:
            break;
        numList = numList + [sumNum]
        count += 1
        if sumNum %2 == 0:
            reslutNum = reslutNum + sumNum
    print(reslutNum)

main()

