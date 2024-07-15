from collections import deque
import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for i in range(1, n+1):
  cnt = 0
  string = input()
  # 홀수개라면 짝이 맞지 않으니 NO 프린트
  if len(string) % 2 != 0:
    print('NO')
    continue
  else:
    # 문자열 순환
    for j in string:
      # cnt가 음수라면 여는괄호 없이 닫는 괄호가 나온 것이기 때문에 짝이 맞지 않음. break
      if cnt < 0:
        break
      # 여는 괄호가 나오면 cnt 1 추가
      if j == '(':
        cnt += 1
      # 닫는 괄호가 나오면 cnt 1 감소
      else:
        cnt -= 1
  # cnt가 0이라는 것은 짝이 다 맞는 것이기 때문에 YES로 바꿈      
  if cnt == 0:
    print('YES')
  else:
    # 그 외의 경우는 모두 'NO' 
    print('NO')