from sys import stdin

def input():
    return stdin.readline().rstrip()

# n=26, m=5
n, m = map(int, input().split())

# 숫자: 이름 딕셔너리
pokemon_dict = {}
# 이름: 숫자 딕셔너리
number_dict = {}

# 1부터 n까지
for i in range(1, n+1):
    pokemon = input()
    # 숫자: 이름 딕셔너리 생성
    pokemon_dict[i] = pokemon
    # 이름: 숫자 딕셔너리 생성
    number_dict[pokemon] = i

# m까지
for _ in range(m):
    # 확인해야 하는 입력 값
    x = input()
    # 숫자라면 pokemon_dict에서 포켓몬 이름을 찾음
    if x.isdigit():
        print(pokemon_dict[int(x)])
    else:
        # 숫자가 아니라면 number_dict에서 숫자를 찾음
        print(number_dict[x])
