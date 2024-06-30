import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

answer = 0

# A,B가 크로스되지 않는 경우 찾기
# ABBA의 경우 크로스되지 않기 때문에 좋은 단어임

for _ in range(n):
  string = input()
  # 첫 문자를 리스트에 넣어둠
  stack = [string[0]]
  # string을 인덱스 1부터 탐색(인덱스 0은 위에서 사용)
  for i in range(1, len(string)):
    # stack에 문자가 있고, 마지막 문자가 현재 문자와 같다면(같은 문자가 연속된다면) 
    if len(stack) != 0 and stack[-1] == string[i]:
      # stack에 있는 문자를 삭제
      stack.pop()
    else:
      # 그렇지 않다면 현재 문자를 stack에 저장
      stack.append(string[i])
  # stack에 요소가 없다면(AA, BB 짝이 모두 맞는다면) answer에 1을 더함  
  if len(stack) == 0:
    answer += 1

print(answer)