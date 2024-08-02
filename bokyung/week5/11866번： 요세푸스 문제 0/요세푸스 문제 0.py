import sys

def input():
  return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
answer = []
tmp = 0

# while len(arr) > 0:
#     if tmp + k - 1 >= len(arr):
#         tmp %= k
#     else:
#         tmp += k - 1
    
#     if len(arr) == k:
#         tmp = k - 1

#     elif len(arr) < k :
#         answer += arr
#         arr = []
#         break

#     answer.append(arr.pop(tmp))

while len(arr) > 0:
    tmp += k - 1
    # 제거해야 하는 인덱스가 어레이 길이 보다 크면 나머지 연산을 한다
    if tmp >= len(arr):
        tmp %= len(arr)

    answer.append(arr.pop(tmp))

# formatted_string = '&lt;' + ', '.join(map(str, answer)) + '&gt;'
formatted_string = '<' + ', '.join(map(str, answer)) + '>'

print(formatted_string)

