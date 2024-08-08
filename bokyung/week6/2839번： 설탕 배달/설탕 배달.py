import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
# answer = 0

# # 5의 배수인 경우, 5로 나눈 몫이 최솟값
# if n % 5 == 0:
#      print(n//5)
# else:
#     # 5보다 큰 수면서 5의 배수가 아닌 경우, 우선 5개를 나눈 몫을 answer에 더한다. 나머지로 올 수 있는 값은 1, 2, 3, 4
#     if n > 5:
#         answer += n // 5
#         n %= 5
#         # 1, 2, 3, 4 중에서 2는 5를 더했을 때 7이므로 해당 값은 3의 배수가 되지 못한다 > -1 출력
#         if n == 2:
#             print(-1) 
#         # 4의 경우, 5를 더하면 9가 되므로 3의 배수가 될 수 있다. answer - 1(5의 배수 1번 뺌) + 3(9//3)    
#         elif n == 4:
#             print(answer+2)
#         # 1, 3의 경우 각각 6이 되고(answer - 1 + 2) 3이 되기 때문에 answer + 1
#         else:
#             print(answer+1)
#     else:
#         # 5보다 작은 수에서 3의 배수인 경우는 3뿐이다
#         if n == 3:
#             print(1)
#         else:
#             print(-1)


# 가능한 5kg 봉지를 최대한 사용 > 5의 배수가 될 때가지 3씩 뺀다
bags = 0
while n >= 0:
    if n % 5 == 0:
        bags += n // 5
        print(bags)
        break
    n -= 3
    bags += 1
else:
    print(-1)  