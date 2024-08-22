import sys

N = int(sys.stdin.readline().strip())

target = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    target.append((x, y))

target.sort()

for x, y in target:
    print(x, y)