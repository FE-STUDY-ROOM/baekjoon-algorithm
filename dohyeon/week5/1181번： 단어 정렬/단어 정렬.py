import sys

N = int(sys.stdin.readline().strip())

target = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    target.append(word)

# 중복 제거
target = list(set(target))

# 정렬 길이순
target.sort(key=lambda x: (len(x), x))


for word in target:
    print(word)