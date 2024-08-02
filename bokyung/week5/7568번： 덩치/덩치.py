import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
arr = []
answer = [1 for _ in range(n)]

for _ in range(n):
  x, y = map(int,input().split())
  arr.append((x,y))

for i in range(n):
  for j in range(n):
    if i != j:
        x, y = arr[i]
        p, q = arr[j]
        # 덩치 비교를 해서 덩치 차이가 나는 경우 answer에서 작은 덩치에 해당하는 인덱스의 값을 1 더한다
        if x > p and y > q:
            answer[j] += 1

print(' '.join(map(str, answer)))