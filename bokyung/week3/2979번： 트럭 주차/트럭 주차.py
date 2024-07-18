import sys

def input():
  return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

time_dict = {}
answer = {}

for _ in range(3):
  start, end = map(int, input().split())

  # 도착 시간 ~ 떠난 시간 -1 까지 트럭이 있었던 시간에 1씩 추가한다 => 이 시간에 트럭이 몇대 있었는지 알 수 있음
  for i in range(start, end):
    time_dict[i] = time_dict.get(i, 0) + 1

# value를 기준으로 다시 딕셔너리를 만든다
# 트럭의 수가 몇분동안 지속되었는지 확인하기 위해서 (value는 1,2,3 중에 하나)
for v in time_dict.values():
  answer[v] = answer.get(v, 0) + 1

# 1인 경우의 값 * a + 2인 경우의 값 * b * 2(요금은 각 트럭별로) + 3인 경우의 값 * c * 3(요금은 각 트럭별로)
print(answer.get(1, 0) * a + answer.get(2, 0) * b * 2 + answer.get(3, 0) * c * 3)