import sys
a,b,c = map(int, sys.stdin.readline().split())

# 주차 시간
parking = [0] * 101

# 주차 시간 입력
for _ in range(3):
    start, end = map(int, sys.stdin.readline().split())
    for i in range(start, end):
        parking[i] += 1

# 주차 요금 계산
total_fee = 0
for i in parking:
    if i == 1:
        total_fee += a
    elif i == 2:
        total_fee += b * 2
    elif i == 3:
        total_fee += c * 3

print(total_fee)
