# from sys import stdin

# def input():
#     return stdin.readline().rstrip()

# n = int(input())
# num_list = []

# # 1~n까지의 숫자 배열 생성
# for i in range(1, n +1):
#     # 어차피 홀수는 답이 될 수 없으니 짝수번째만 확인
#     if i % 2 == 0:
#         num_list.append(i)

# # 숫자 배열 길이가 1이 될 때까지 while문 반복
# while(len(num_list) > 1):
#     # 직전 배열의 길이가 짝수인 경우 처음과 같이 진행(숫자 삭제하고 뒤로 보내고 > 홀수번째 인덱스만)
#     if n % 2 == 0:
#         n = len(num_list)
#         num_list = num_list[1::2]
#     else:
#         # 직전 배열의 길이가 홀수인 경우 짝수번째 인덱스만)
#         n = len(num_list)
#         num_list = num_list[0::2]

# print(num_list[0])

# 처음에는 while문으로 시도했는데 테스트 케이스는 통과했지만 백준 사이트에서 시간초과로 실패가 떴다

# 이진탐색을 시도했으나 큐를 이용해서 해결하는 듯 하다..

from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()  # 제일 위의 카드를 버림
    queue.append(queue.popleft())  # 제일 위의 카드를 제일 아래로 옮김

print(queue[0])


# 리스트를 이용하여 pop, append했을 때와 큐를 이용했을 때의 차이

# Deque (큐) 사용:
# popleft()와 append()는 O(1) 시간 복잡도를 가집니다.
# 큐의 길이가 1이 될 때까지 반복하여 최종적으로 O(N) 시간 복잡도를 가집니다.

# 리스트 사용:
# pop(0) 연산은 O(N) 시간 복잡도를 가집니다.
# 리스트의 길이가 1이 될 때까지 반복하여 최종적으로 O(N^2) 시간 복잡도를 가집니다.