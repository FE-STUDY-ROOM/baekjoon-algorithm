import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
answer = []

for _ in range(n):
    number = int(input())
    answer.append(number)

for i in sorted(answer):
   print(i)
       