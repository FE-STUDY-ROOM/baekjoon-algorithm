import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
answer = []

for _ in range(n):
    x, y = map(int, input().split())
    answer.append((x, y))

answer = sorted(answer, key=lambda x: (x[1], x[0]))

for x, y in answer:
   print(x, y)
