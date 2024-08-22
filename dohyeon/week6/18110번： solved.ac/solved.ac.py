import sys

n = int(sys.stdin.readline().strip())

target = []

for _ in range(n):
    voc = int(sys.stdin.readline().strip())
    target.append(voc)

if n == 0:
    print(0)
else:
    target.sort()
    
    delete = round(n * 0.15)
    answer = target[delete:len(target)-delete]

    average = round(sum(answer) / len(answer))

    print(average)