def solution(n):
    arr = [n]
    for i in str(n):
        arr.append(int(i))

    return min(arr)


print(solution(216))
