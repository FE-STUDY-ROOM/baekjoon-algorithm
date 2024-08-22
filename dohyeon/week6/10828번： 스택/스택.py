import sys

N = int(sys.stdin.readline().strip())
target = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        target.append(int(command[1]))
    
    elif command[0] == 'pop':
        if target:
            print(target.pop())
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(target))
    
    elif command[0] == 'empty':
        print(1 if not target else 0)
    
    elif command[0] == 'top':
        if target:
            print(target[-1])
        else:
            print(-1)