def is_good_word(word):
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return not stack


n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    if is_good_word(word):
        count += 1

print(count)
