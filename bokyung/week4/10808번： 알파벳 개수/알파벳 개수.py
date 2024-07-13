import sys

def input():
  return sys.stdin.readline().rstrip()

# 문자가 나온 횟수를 저장할 딕셔너리
alpha_dict = {} 
string = input()

# 문자를 탐색하면서 나오면 1씩 추가한다
for i in string:
  alpha_dict[i] = alpha_dict.get(i, 0) + 1

# a~z까지 탐색하면서 해당 값을 키로하는 alpha_dict의 값을 출력한다. 없으면 0 출력(get 함수)
for i in 'abcdefghijklmnopqrstuvwxyz':
  print(alpha_dict.get(i, 0), end=' ')