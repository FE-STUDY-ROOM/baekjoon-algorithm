def main():
    # 1. 입력값을 배열로 만든다
    import sys
    input = sys.stdin.read
    data = input().split()

    # 2. 입력값의 0과 1은 각각 N과 M으로 도감의 크기와 문제의 갯수다
    N = int(data[0])
    M = int(data[1])

    # 3. 풀어야할 문제는 문자와 숫자의 혼합으로 매핑을 하기 위해 딕셔너리를 두 개 만든다
    # 하나의 딕셔너리는 포켓몬-번호, 다른 하나는 번호-포켓몬이다
    pokemons_by_number = {}
    pokemons_by_name = {}

    # 4. 0과 1은 N과 M으로 실질적인 시작 인덱스는 2가 된다
    index = 2

    # 5. for문으로 1부터 N + 1까지 순환을 한다
    # 순환을 하면서 두 개의 딕셔너리를 각각 채워넣고, index의 값을 증가시킨다
    # 순환이 끝나면 index의 값은 M의 시작점에 위치하게 된다
    for i in range(1, N + 1):
        name = data[index]
        pokemons_by_number[str(i)] = name
        pokemons_by_name[name] = str(i)
        index += 1

    # 6. 정답을 담기 위한 배열이다
    results = []

    # 7. for문을 M만큼 도는데 이때 증가했던 index를 활용해 매핑을 한다.
    for j in range(M):
        query = data[index]
        if query.isdigit():  # 숫자인 경우 번호로 이름 찾기
            results.append(pokemons_by_number[query])
        else:  # 문자열인 경우 이름으로 번호 찾기
            results.append(pokemons_by_name[query])
        index += 1

    # 8. 입력된 값을 원하는 형태로 변환한다.
    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == "__main__":
    main()
