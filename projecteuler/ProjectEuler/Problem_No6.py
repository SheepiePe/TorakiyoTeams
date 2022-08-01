"""
最初の10個の自然数について, その二乗の和は,
1^2 + 2^2 + ... + 10^2 = 385

最初の10個の自然数について, その和の二乗は,
(1 + 2 + ... + 10)^2 = 3025

これらの数の差は 3025 - 385 = 2640 となる.
同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
"""

COUNT = 100
powSum = 0
sumPow = 0

for i in range(1,COUNT + 1):
    powSum = powSum + i ** 2

for i in range(1, COUNT + 1):
    sumPow = sumPow + i

sumPow = sumPow ** 2

print(sumPow - powSum)