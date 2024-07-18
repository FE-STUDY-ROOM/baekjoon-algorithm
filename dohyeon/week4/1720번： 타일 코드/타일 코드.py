import sys

n = int(sys.stdin.readline().rstrip())

DP = [0]*31

DP[1]=1
DP[2]=3

for i in range(3,n+1):
    DP[i] = DP[i-1] + 2*DP[i-2]

if n>=3:
    if n%2==0:
        print((DP[n] - (2*DP[(n-2)//2] + DP[n//2]))//2 + (2*DP[(n-2)//2] + DP[n//2]))
    else:
        print((DP[n] - DP[(n-1)//2])//2 + DP[(n-1)//2])
else:
    print(DP[n])