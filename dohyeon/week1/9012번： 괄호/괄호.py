# 정수로 입력받기
import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    # 한줄씩 입력받기
    word = sys.stdin.readline().strip()
    
    # 스택 초기화
    stack = []
    for char in word:
      if char == '(':
          stack.append(char)
      elif char == ')':
          if stack and stack[-1] == '(':
              stack.pop()
          else:
              stack.append(char)
    if not stack:
        print("YES")
    else:
        print("NO")