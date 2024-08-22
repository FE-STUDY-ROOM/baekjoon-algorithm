import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
# 문자열을 받을 리스트를 리스트가 아닌 셋으로 받는다(중복처리를 위해서)
answer = set()

for _ in range(n):
  answer.add(input())

# 문자열 set을 1순위 길이, 2순위 문자열로 정렬한다
answer = sorted(answer, key=lambda x: (len(x), x))

for i in answer:
  print(i)


