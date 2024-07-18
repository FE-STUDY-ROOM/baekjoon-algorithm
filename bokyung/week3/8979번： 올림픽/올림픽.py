import sys

def input():
  return sys.stdin.readline().rstrip()

count, target = map(int, input().split())
index = -1

# [국가번호, 금메달 수, 은메달 수, 동메달 수] 이중 배열
medals = [list(map(int, input().split())) for _ in range(count)]
# [[1, 1, 2, 0], [2, 0, 1, 0], [3, 0, 1, 0], [4, 0, 0, 1]]

# 리스트를 정렬한다. 이렇게 하면 금메달 수 > 일치하면 은메달 수 > 일치하면 동메달 수를 기준으로 정렬한다
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# 정렬된 리스트에서 target의 인덱스를 찾는다
for i in range(count):
  if medals[i][0] == target:
    index = i
    break

# 찾은 인덱스의 메달 개수와 일치하는 첫번째 요소의 인덱스+1을 반환한다
for i in range(count):
  if medals[index][1:] == medals[i][1:]:
    print(i+1)
    break