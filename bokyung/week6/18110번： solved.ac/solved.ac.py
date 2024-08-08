# import sys

# def input():
#   return sys.stdin.readline().rstrip()

# n = int(input())

# # 백준 런타임 에러: 1차(10분)
# # score = []

# # for _ in range(n):
# #     score.append(int(input()))

# # score.sort()
# # count_list = score[round(n*0.15) : n-round(n*0.15)]

# # print(round(sum(count_list)/len(count_list)))


# # 백준 런타임 에러: 2차(+30분) 
# score = {}
# sum_score = 0
# # 제외되는 인원 수
# no_count = round(n*0.15)
# # 제외된 인원 수
# low = high = 0

# if n == 0:
#     print(0)
#     sys.exit()

# for _ in range(n):
#     num = int(input())
#     score[num] = score.get(num, 0) + 1
#     sum_score += num

# min_score = min(score)
# max_score = max(score)

# while low != no_count:
#     if score.get(min_score, 0) >= low:
#         sum_score -= min_score * (no_count - low)
#         low = no_count
#     else:
#         sum_score -= min_score * score.get(min_score, 0)
#         low += score.get(min_score, 0)
#         min_score += 1

# while high != no_count:
#     if score.get(max_score, 0) >= high:
#         sum_score -= max_score * (no_count - high)
#         high = no_count
#     else:
#         sum_score -= max_score * score.get(max_score, 0)
#         high += score.get(max_score, 0)
#         max_score -= 1

# print(round(sum_score/(n - no_count*2)))


import sys

def input():
  return sys.stdin.readline().rstrip()

#NOTE: 반올림 오차: round()는 반올림할 때 가장 가까운 수로 올림합니다. .5의 경우, Python은 짝수 방향으로 반올림하는 "은행가의 반올림" 방식을 사용합니다. 예를 들어, round(2.5)는 2가 되고 round(3.5)는 4가 됩니다.
def custom_round(number):
    if number >= 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)

n = int(input())

# 0인 경우 예외처리
if n == 0:
    print(0)
    sys.exit()

score = []

for _ in range(n):
    score.append(int(input()))

score.sort()
count_list = score[custom_round(n*0.15) : n-custom_round(n*0.15)]

if count_list:
    print(custom_round(sum(count_list)/len(count_list)))
else:
    # 전부 절사된 경우
    print(0)