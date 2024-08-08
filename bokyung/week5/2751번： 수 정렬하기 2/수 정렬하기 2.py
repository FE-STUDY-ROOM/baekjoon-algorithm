# import sys

# def input():
#   return sys.stdin.readline().rstrip()

# n = int(input())
# answer = []

# for _ in range(n):
#     number = int(input())
#     answer.append(number)

# for i in sorted(answer):
#    print(i)


# 이진탐색 라이브러리를 이용했는데, 백준 사이트에서는 시간초과가 나옵니다..
import sys
from bisect import insort_left

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
answer = [int(input())]

for _ in range(n-1):
    insort_left(answer, int(input()))

for i in answer:
    print(i)