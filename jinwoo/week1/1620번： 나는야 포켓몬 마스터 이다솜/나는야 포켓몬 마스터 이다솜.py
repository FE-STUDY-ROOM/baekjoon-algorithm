# 입력값
pokemon_list = [
    "Bulbasaur", "Ivysaur", "Venusaur",
    "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise",
    "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill",
    "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate",
    "Spearow", "Fearow",
    "Ekans", "Arbok",
    "Pikachu", "Raichu"
]

problem_list = [
    25,
    "Raichu",
    3,
    "Pidgey",
    "Kakuna"
]

# 문제풀이


def solution(n, m):
    answer = []

    # 1. 맵핑을 위한 객체를 두 개 준비한다. 하나의 객체는 num-str 형식이고, 다른 하나는 str-num 형식이다.
    dict1 = {}
    dict2 = {}

    # 2. for-in으로 입력값을 순환하면서 앞에 만들어둔 두 객체를 채운다. 인덱스값도 필요하기 때문에 enumerate를 사용한다.
    for i, p in enumerate(pokemon_list):
        dict1[i + 1] = p
        dict2[p] = i + 1

    # 3. for-in으로 입력값을 순환하면서 값이 숫자 혹은 문자인지 확인하고 그에 맞는 값을 맵핑하여 반환한다.
    for i in problem_list:
        if isinstance(i, int):
            answer.append(dict1[i])
        else:  # 문자
            answer.append(dict2[i])

    return answer


print(solution(pokemon_list, problem_list))
