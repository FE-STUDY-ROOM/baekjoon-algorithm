import sys


def is_balanced(string):
    stack = []
    for char in string:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return not stack


input = sys.stdin.read
data = input().splitlines()

for line in data:
    if line == ".":
        break
    if is_balanced(line):
        print("yes")
    else:
        print("no")
