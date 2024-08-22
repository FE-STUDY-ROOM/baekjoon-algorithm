import sys

target = int(sys.stdin.readline().strip())

count = 0

while target >= 0:
    if target % 5 == 0:
        count += target // 5
        print(count)
        break
    
    target -= 3
    count += 1

else:
    print(-1)