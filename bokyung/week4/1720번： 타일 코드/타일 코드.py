import sys

def input():
  return sys.stdin.readline().rstrip()

# n = int(input())
# answer = 0

# answer += (n//2) * 2 * 2 + n % 2

# print(answer)

# 잘 모르겠다... 
# https://velog.io/@longinus99/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1720-%ED%83%80%EC%9D%BC%EC%BD%94%EB%93%9C-Python
n = int(input())

d = [0 for _ in range(n+1)]

d[0] = 1
d[1] = 1

tmp = 2

while tmp < n + 1: 
  d[tmp] = d[tmp-1] + 2*d[tmp-2]
  tmp += 1

if n %2 == 0 :
  print((d[n] + d[n//2] + 2*d[(n-2)//2])//2)
else:
  print((d[n] + d[(tmp-1)//2] )//2) 