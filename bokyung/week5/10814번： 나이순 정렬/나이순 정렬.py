import sys
from bisect import bisect_right

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
answer = []
# 나이를 담아 둘 리스트 (나이 기준으로 하기 때문에)
age_list = []

for _ in range(n):
    age, name = input().split()
    if len(answer) == 0:
        answer.append([int(age), name])
        age_list.append(int(age))
    else:
       # 나이를 기준으로 들어갈 인덱스를 찾음. 나이가 같다면 먼저 입력된 값이 앞으로 오기 때문에 현재 값은 맨 뒤로 > bisect_right 사용
       index = bisect_right(age_list, int(age))
       # 찾은 인덱스에 맞게 answer에 추가
       answer.insert(index, [int(age), name])
       # age_list에도 추가
       age_list.insert(index, int(age))

# 이거는 시간초과가 나옵니당
# answer = sorted(answer, key=lambda x: (x[0], answer.index(x)))

for i in answer:
  print(i[0], i[1])