import sys
# 정수로 입력받기
n = int(sys.stdin.readline().strip())

# 1000까지의 삼각수를 미리 구해놓기
tri_list = []
for i in range(1, 45):
    tri_list.append(i * (i + 1) // 2)

# 각 테스트케이스에 대해 결과 계산
for _ in range(n):
    # 한줄씩 입력받기
    target = int(sys.stdin.readline().strip())
    
    # 3개의 삼각수 합으로 표현 가능한지 확인
    result = False
    for i in tri_list:
        for j in tri_list:
            for k in tri_list:
                if i + j + k == target:
                    result = True
                    break
            if result:
                break
        if result:
            break

    # 결과 출력
    if result:
        print(1)
    else:
        print(0)