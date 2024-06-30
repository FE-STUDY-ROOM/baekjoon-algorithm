# 정수로 입력받기
import sys
n = int(sys.stdin.readline().strip())
cnt = 0

for _ in range(n):
  s = sys.stdin.readline().strip()
  stack = []

  for i in range(len(s)):
    if stack and s[i] == stack[-1]:
      stack.pop()
    else:
      stack.append(s[i])
  if not stack:
    cnt += 1
print(cnt)