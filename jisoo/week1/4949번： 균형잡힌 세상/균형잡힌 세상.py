import sys

while True:
  word = input()
  stack = []

  if word == '.':
    break

  for w in word:
    if w == '(' or w == '[':
      stack.append(w)
    elif w == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(w)
    elif w == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(w)
  
  if not stack:
    print('yes')
  else:
    print('no')
  