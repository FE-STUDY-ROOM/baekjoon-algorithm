import sys

while True :
  target = sys.stdin.readline().rstrip()
  if target == '.':
    break
  stack = []
  answer = 'yes'
  
  for i in range(len(target)):
    if target[i] == '(' or target[i] == '[':
      stack.append(target[i])
    elif target[i] == ')':
      if not stack or stack[-1] == '[':
        answer = 'no'
        break
      elif stack[-1] == '(':
        stack.pop()
    elif target[i] == ']':
      if not stack or stack[-1] == '(':
        answer = 'no'
        break
      elif stack[-1] == '[':
        stack.pop()
  if stack:
    answer = 'no'

  print(answer)
