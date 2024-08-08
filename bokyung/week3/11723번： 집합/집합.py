import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

S = []

for _ in range(n):
  check = input().split()
  if check[0] == 'add':
    if int(check[1]) not in S:
      S.append(int(check[1]))
  elif check[0] == 'remove':
    if int(check[1]) in S:
      S.remove(int(check[1]))
  elif check[0] == 'check':
    if int(check[1]) in S:
      print(1)
    else:
      print(0)
  elif check[0] == 'toggle':
    if int(check[1]) in S:
      S.remove(int(check[1]))
    else:
      S.append(int(check[1]))
  elif check[0] == 'all':
    S = [x for x in range(1,21)]
  else:
    S = []