import sys, re

def input():
  return sys.stdin.readline().rstrip()

for i in range(10000):
  string = input()
  # input 종료면 종료.
  if string == '.':
    break

  # small_cnt = 0 # () cnt
  # big_cnt = 0 # [] cnt

  # 괄호를 제외한 문자는 모두 삭제
  string = re.sub('[^\(\)\[\]]','', string)
  # 괄호가 없는 문자열인 경우 'yes' 출력
  if len(string) == 0:
    print('yes')
  else:
    # 짝이 맞는 괄호를 삭제
    for _ in range(len(string)):
      string = string.replace('()', '')
      string = string.replace('[]', '')

    # for문 종료 후 길이가 0이 아니라면 짝이 맞지 않는 것이기 때문에 no
    if len(string):
      print('no')
    # 0인 경우 yes
    else:
      print('yes')

      
    # for j in range(len(string)):
    #   if string[j] == '(':
    #     small_cnt += 1
    #   elif string[j] == ')':
    #     small_cnt -= 1
    #   elif string[j] == '[':
    #     big_cnt += 1
    #   else:
    #     big_cnt -= 1
      
    #   # 여는 괄호와 닫는 괄호 짝이 안 맞는 경우
    #   if string[j-1] in ['(','[']:
    #     if string[j-1] == '(' and string[j] == ']':
    #       print('no')
    #       break
    #     elif string[j-1] == '[' and string[j] == ')':
    #       print('no')
    #       break

    #   # 짝이 안 맞는 경우 no
    #   if small_cnt < 0 or big_cnt < 0:
    #     print('no')
    #     break

    # if small_cnt == 0 and big_cnt == 0:
    #   print('yes')

  