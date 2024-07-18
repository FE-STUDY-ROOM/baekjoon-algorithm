import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

input = sys.stdin.readline

a = int(input())
b = int(input())

check = [2, 3, 5, 7, 11, 13, 17]  # 소수
pera = a / 100.0
perb = b / 100.0
sa = sb = 0

# 확률 구하는 공식
# p(k) = 18Ck * P^k * (1-p)^(18-k)
for i in check:
    combi = combination(18, i)
    sa += combi * power(pera, i) * power(1.0 - pera, 18 - i)
    sb += combi * power(perb, i) * power(1.0 - perb, 18 - i)

result = sa + sb - sa * sb
print("{:.16f}".format(result))