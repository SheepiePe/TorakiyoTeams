"""
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.
10 001 番目の素数を求めよ.
"""
import sympy

MAXCOUNT = 10001

def main(maxCount):
    print(sympy.prime(maxCount))



main(MAXCOUNT)