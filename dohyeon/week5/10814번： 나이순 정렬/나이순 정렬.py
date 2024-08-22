import sys

N = int(sys.stdin.readline().strip())

target = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    target.append((int(age), name, i))

target.sort(key=lambda x: (x[0], x[2]))

for age, name, _ in target:
    print(age, name)