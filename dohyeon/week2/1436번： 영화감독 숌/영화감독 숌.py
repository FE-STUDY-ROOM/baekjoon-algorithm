import sys
target = int(sys.stdin.readline().strip())

num = 0
count = 0

while True:
    if '666' in str(num):
        count += 1
    if count == target:
        print(num)
        break
    num += 1
