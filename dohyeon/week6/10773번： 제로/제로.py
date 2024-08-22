import sys

K = int(sys.stdin.readline().strip())

target = []

for _ in range(K):
    num = int(sys.stdin.readline().strip())
    
    if num == 0:
        if target:  
            target.pop()
    else:
        target.append(num)

print(sum(target))