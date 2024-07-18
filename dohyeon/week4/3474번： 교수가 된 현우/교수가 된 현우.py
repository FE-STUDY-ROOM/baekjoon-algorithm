import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
  target = int(sys.stdin.readline().rstrip())
  count = 0
  i = 5
  while i <= target:
      count += target // i
      i *= 5
  print(count)