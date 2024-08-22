import sys
height_list = []

# 한줄씩 9번 입력받아서 height_list에 추가
for _ in range(9):
    height = int(sys.stdin.readline().strip())
    height_list.append(height)

# 9개의 키 중 2개를 뽑아서 합이 100이 되는 경우를 찾아서 제거
for i in height_list:
    for j in height_list:
        # 같은 키는 제외
        if i == j:
            continue
        # 2개의 키를 제외한 나머지 키들의 합이 100이면 제거
        if sum(height_list) - i - j == 100:
            height_list.remove(i)
            height_list.remove(j)
            break
    # 7개의 키가 남으면 종료
    if len(height_list) == 7:
        break

# 오름차순 정렬
height_list.sort()

# 결과 출력
for height in height_list:
    print(height)