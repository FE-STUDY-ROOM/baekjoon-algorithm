import sys

def input():
  return sys.stdin.readline().rstrip()

string = input()
# 초기값을 1로 설정하여 팰린드롬인 경우 1 출력
answer = 1

# 주어진 문자의 절반까지만 확인한다. 홀수인 경우 어차피 한개만 나오기 때문에 그전까지만 탐색
for i in range(0, len(string)//2):
  # 단어의 앞과 뒤를 동시에 보면서 같은 값인지를 확인한다.
  if string[i] != string[len(string)-1-i]:
    # 일치하지 않는 경우 팰린드롬이 아니기 때문에 answer를 0으로 변경하고 for문을 빠져나온다
    answer = 0
    break

print(answer)
