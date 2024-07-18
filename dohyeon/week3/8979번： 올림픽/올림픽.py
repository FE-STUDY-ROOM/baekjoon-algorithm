# 국가의 수, 등수를 알고 싶은 국가 입력

import sys
n, k = map(int, sys.stdin.readline().split())

# 등수 입력 배열
rank = []

# 국가, 금메달, 은메달, 동메달 입력
for _ in range(n):
    country, gold, silver, bronze = map(int, sys.stdin.readline().split())
    rank.append([country, gold, silver, bronze])

# 메달 수에 따라 정렬
# 금메달 -> 은메달 -> 동메달 순으로 내림차순 정렬
rank.sort(key=lambda x: (-x[1], -x[2], -x[3]))

print(rank)
# 등수를 알고 싶은 국가의 메달 정보
for i in range(n):
    if rank[i][0] == k:
        k_gold, k_silver, k_bronze = rank[i][1], rank[i][2], rank[i][3]
        k_rank = i
        break

# 등수 계산
rank_count = 1
for i in range(k_rank):
    if rank[i][1] > k_gold:
        rank_count += 1
    elif rank[i][1] == k_gold:
        if rank[i][2] > k_silver:
            rank_count += 1
        elif rank[i][2] == k_silver:
            if rank[i][3] > k_bronze:
                rank_count += 1

print(rank_count)


# 정렬 기준

# -x[1]: 금메달 수를 기준으로 내림차순 정렬합니다. x[1]은 금메달 수인데, -x[1]으로 부호를 바꾸어줍니다. sort() 메소드는 기본적으로 오름차순(작은 값에서 큰 값)으로 정렬하기 때문에, -x[1]으로 하면 금메달 수가 큰 값이 작은 값보다 앞으로 오게 됩니다.
# -x[2]: 은메달 수를 기준으로 내림차순 정렬합니다. 금메달 수가 동일한 경우 은메달 수를 비교합니다. 마찬가지로, -x[2]로 하여 은메달 수가 큰 값이 앞에 오도록 합니다.
# -x[3]: 동메달 수를 기준으로 내림차순 정렬합니다. 금메달과 은메달 수가 동일한 경우 동메달 수를 비교합니다. -x[3]으로 하여 동메달 수가 큰 값이 앞에 오도록 합니다.

# 정리
# 따라서, rank.sort(key=lambda x: (-x[1], -x[2], -x[3])) 코드는 금메달 수, 은메달 수, 동메달 수를 차례로 비교하여 내림차순으로 정렬합니다. 즉, 금메달 수가 많은 순서대로, 금메달 수가 같으면 은메달 수가 많은 순서대로, 그것도 같으면 동메달 수가 많은 순서대로 정렬하게 됩니다.

