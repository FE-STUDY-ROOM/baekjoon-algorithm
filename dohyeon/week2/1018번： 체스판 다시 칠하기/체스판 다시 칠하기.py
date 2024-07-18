import sys
n, m = map(int, sys.stdin.readline().split())

board = []

# 보드 입력
for _ in range(n):
    board.append(sys.stdin.readline().strip())

# 8x8 체스판을 만들 수 있는 모든 경우의 수
cases = []

# 8x8 체스판을 만들 수 있는 모든 경우의 수를 구함
for i in range(n - 7):
    for j in range(m - 7):
      # case1: 첫 번째 칸이 W인 경우
      # case2: 첫 번째 칸이 B인 경우
        case1 = 0
        case2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                # 행과 열의 합이 짝수인 경우
                if (k + l) % 2 == 0:
                    # W로 시작하는 경우
                    if board[k][l] != 'W':
                        case1 += 1
                    # B로 시작하는 경우
                    if board[k][l] != 'B':
                        case2 += 1
                # 행과 열의 합이 홀수인 경우
                else:
                    if board[k][l] != 'B':
                        case1 += 1
                    if board[k][l] != 'W':
                        case2 += 1
        cases.append(case1)
        cases.append(case2)

# case1과 case2 중 작은 값을 print
print(min(cases))
