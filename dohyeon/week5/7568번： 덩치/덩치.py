import sys

N = int(sys.stdin.readline().strip())

target = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    target.append((weight, height))

ranks = []

# 덩치 등수를 계산
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if target[j][0] > target[i][0] and target[j][1] > target[i][1]:
                rank += 1
    ranks.append(rank)


print(' '.join(map(str, ranks)))