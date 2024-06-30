# 정수 26, 5를 N, M으로 입력받기
import sys
N, M = map(int, sys.stdin.readline().split())

# pocketmon_name = { 포켓몬 이름 : 번호 }
# pocketmon_number = { 번호 : 포켓몬 이름 }
poketmon_name = dict()
poketmon_number= dict()

for i in range(1, N+1):
    poketmon = sys.stdin.readline().strip()
    # poketmon_name = { Bulbasaur: 1 }
    poketmon_name[i] = poketmon
    # poketmon_number = { 1: Bulbasaur }
    poketmon_number[poketmon] = i

for i in range(M):
    find = sys.stdin.readline().strip()
    if find[0].isalpha():
        print(poketmon_number[find]) 
    else:
        print(poketmon_name[int(find)])