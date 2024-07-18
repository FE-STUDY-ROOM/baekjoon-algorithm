import sys
word = sys.stdin.readline().rstrip()

# 문자열을 뒤집어서 같으면 1 다르면 0
if word == word[::-1]:
  print(1)
else:
  print(0)

