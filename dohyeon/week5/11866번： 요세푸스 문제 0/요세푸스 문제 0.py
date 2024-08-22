import sys

N, K = map(int, sys.stdin.readline().split())

target = list(range(1, N+1))

result = []

index = 0

while target:
    index = (index + K - 1) % len(target)
    
    result.append(str(target.pop(index)))

print("<" + ", ".join(result) + ">")