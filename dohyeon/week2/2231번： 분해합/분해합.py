import sys
n = int(sys.stdin.readline().strip())

for i in range(10):
  for j in range(10):
    for k in range(10):
      if i + j + k + int(str(i) + str(j) + str(k)) == n:
        print(int(str(i) + str(j) + str(k)))
        sys.exit(0)

        
        