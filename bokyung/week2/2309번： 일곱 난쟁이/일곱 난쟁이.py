import sys

def input():
  return sys.stdin.readline().rstrip()

height_list = []
# count = 0
answer = []

for _ in range(9):
  height_list.append(int(input()))

height_list.sort()

# 탐색하는 함수 생성
def dfs(depth, start):
    # 7번 진행했을 때
    if depth == 7:  
        # sum이 100 이면 값을 print
        if sum(answer) == 100:
            for j in answer:  
                print(j)
            exit() # 코드 종료
        else: # 7명인데 100이 아니라면
           return # 재귀종료
        
    # depth가 7이 아닌 경우(아직 7번 하지 못한 경우)
    for i in range(start, len(height_list)): 
        answer.append(height_list[i]) # answer에 값을 추가
        dfs(depth + 1, i + 1) # 다음 dfs 실행
        answer.pop() # 위의 dfs를 실행했을 때 함수가 종료되지 않았다면 마지막 값을 제거


dfs(0, 0) 


# sumList = sum(height_list)

# 전체에서 2개를 뺀 값이 100이면 그 두 숫자를 제외한 리스트를 반환한다
# for i in range(len(height_list)):
#   for j in range(i+1, len(height_list)):
#     if sumList - height_list[i] - height_list[j] == 100:
#       # j의 인덱스가 더 크기 때문에 j 먼저 제거
#       height_list.pop(j)
#       height_list.pop(i)
#       break

# for i in range(len(height_list)):
#   print(height_list[i])


# 하나씩 더하면서 계산. 길이가 7이 되었을 때 합을 구한다. 100이 아닌 경우 마지막에 추가한 값을 빼고 그 다음 값을 더한다
# for i in range(9):
#   count += height_list[i]
#   if count > 100:
#     count -= height_list[i]
#   else:
#     answer.append(height_list[i])
#   if i == 9 and count != 100:
#     pass

# print(sum(answer))

# for i in range(len(answer)):
#   print(answer[i])
