import sys

N = int(sys.stdin.readline().strip())

target = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    target.append((x, y))

target.sort(key=lambda point: (point[1], point[0]))

for x, y in target:
    print(x, y)