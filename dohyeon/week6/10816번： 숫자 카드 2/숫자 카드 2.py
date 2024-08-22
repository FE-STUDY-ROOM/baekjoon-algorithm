import sys

N = int(sys.stdin.readline().strip())

cards = list(map(int, sys.stdin.readline().split()))

target = {}
for card in cards:
    if card in target:
        target[card] += 1
    else:
        target[card] = 1

M = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().split()))

result = []
for num in numbers:
    if num in target:
        result.append(str(target[num]))
    else:
        result.append('0')

print(' '.join(result))