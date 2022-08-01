"""
10未満の自然数のうち, 
3もしくは5の倍数になっているものは 3,5,6,9の4つがあり, これらの合計は23になる.
同じようにして, 1000 未満の3か5の倍数になっている数字の合計を求めよ.
"""

import numbers
def main():
    numberSum = 0
    numberSum = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]

    print(sum(numberSum))

main()