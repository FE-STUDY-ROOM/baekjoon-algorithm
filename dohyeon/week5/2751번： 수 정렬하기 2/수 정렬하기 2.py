import sys

N = int(sys.stdin.readline().strip())

target = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    target.append(num)

target.sort()

for num in target:
    print(num)