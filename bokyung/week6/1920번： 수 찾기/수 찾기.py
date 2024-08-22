import sys

def input():
  return sys.stdin.readline().rstrip()

# 백준 시간초과
# n = int(input())
# num_list = list(map(int, input().split()))
# m = int(input())
# check_list =list(map(int, input().split()))

# for i in check_list:
#   if i in num_list:
#     print(1)
#   else:
#     print(0)

n = int(input())
# 주어진 수들을 set에 저장합니다. 
# set 자료구조는 평균적으로 O(1) 시간 복잡도로 멤버십 테스트(숫자가 존재하는지 확인)를 할 수 있습니다. 
# 이는 리스트에서 숫자를 찾는 O(N) 복잡도보다 훨씬 빠릅니다.
num_list = set(map(int, input().split()))
m = int(input())
check_list = map(int, input().split())

for i in check_list:
  if i in num_list:
    print(1)
  else:
    print(0)
  