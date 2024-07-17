import sys

def input():
  return sys.stdin.readline().rstrip()

# def factorial(n):
#   if n == 1:
#     return 1
#   else:
#     return n * factorial(n-1)

n = int(input())

for _ in range(n):
  number = int(input())
  answer = 0
  i = 5
  # 주어진 수를 소인수분해 해서 5의 배수의 합 구하기
  while number >= i:
    answer += number // i
    i *= 5

  print(answer)

# for i in range(1,302, 50):
#   answer = factorial(i)
#   print(i, answer)

# 5의 배수를 기준으로 0의 개수가 정해짐
# > 단순히 5의 배수를 구하는 것이 아니라 소인수분해하듯 누적했어야 함