import sys

N = int(sys.stdin.readline().strip())

target = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().split()))

for num in numbers:
    if num in target:
        print(1)
    else:
        print(0)