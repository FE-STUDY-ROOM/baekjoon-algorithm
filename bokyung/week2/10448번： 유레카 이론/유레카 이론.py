import sys
import itertools 

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

# 삼각수 값들이 들어 있는 리스트
t_list = [1]

# 자연수가 주어졌을 때 그 자연수가 3개의 삼각수의 합으로 이뤄지는 지 확인
# 삼각수의 합이 담긴 리스트를 구하고 > 그중 3개를 뽑아서 합을 구했을 때 입력한 값과 일치하는지 확인

# 삼각수를 구해서 t_list에 추가하는 함수
def triangle():
  t_list.append(t_list[-1] + len(t_list)+1)

for i in range(1, n+1):
  num = int(input())
  # 0으로 초기화
  answer = 0

  # 현재 구해진 삼각수의 최댓값이 입력받은 값보다 작으면 필요한 삼각수를 더 계산한다
  while max(t_list) < num :
    triangle()

  # 중복조합을 이용하여 3개 삼각수를 꺼낸다 => 각 값이 모두 다를 필요가 없기 때문에 중복조합 사용
  for j in itertools.combinations_with_replacement(t_list, 3):
    # 중복조합을 통해 구한 값이 원하는 값과 일치하면 answer에 1을 할당하고 for문을 종료한다 
    if sum(j) == num:
      answer = 1
      break
  # 일치하는 조합이 있었다면 1 없었다면 0을 출력한다
  print(answer)
