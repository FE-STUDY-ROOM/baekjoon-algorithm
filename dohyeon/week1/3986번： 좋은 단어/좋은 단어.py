import sys
# 정수로 입력받기
n = int(sys.stdin.readline().strip())

# 좋은 단어의 개수
nice_word = 0

# 단어의 개수만큼 반복
for _ in range(n):
    # 한줄씩 입력받기
    word = sys.stdin.readline().strip()
    # 스택 초기화
    stack = []
    for char in word:
        # 스택이 비어있지 않고, 스택의 마지막 문자와 현재 문자가 같다면
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    # 스택이 비어있다면 좋은 단어
    if not stack:
        nice_word += 1

print(nice_word)


