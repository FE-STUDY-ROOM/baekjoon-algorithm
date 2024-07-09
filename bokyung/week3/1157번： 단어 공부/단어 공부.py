import sys

def input():
  return sys.stdin.readline().rstrip()

# 입력받은 문자를 모두 소문자로 바꾼다
string = input().lower()

# 문자의 count를 저장할 딕셔너리 생성
str_dict = {}

# 문자를 탐색하면서 나온 횟수를 딕셔너리에 저장(나올때마다 1 증가)
for i in string:
  str_dict[i] = str_dict.get(i, 0) + 1

# 딕셔너리를 값(카운트)을 기준으로 내림차순으로 정렬한다 
sorted_list = sorted(str_dict, key= lambda x: str_dict[x], reverse=True)

# 값이 동일한 키가 있는지 확인한다
if len(sorted_list) > 1 and str_dict[sorted_list[0]] == str_dict[sorted_list[1]]:
  # 동일한 값이 있다면(카운트가 일치한다면) ? 리턴
  print('?')
else:
  # 유일한 값이라면 해당 문자를 대문자로 리턴
  print(sorted_list[0].upper())