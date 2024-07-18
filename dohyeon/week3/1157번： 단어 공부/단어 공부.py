import sys
string = sys.stdin.readline().strip()

# 대소문자 구분하지 않기 위해 대문자로 변환 (출력시 대문자로 출력해야 하므로)
target = string.upper()

# 각 알파벳의 개수를 저장할 딕셔너리
count_dictionary = {}

# 각 알파벳의 개수를 딕셔너리에 저장
for i in target:
    if i in count_dictionary:
        count_dictionary[i] += 1
    else:
        count_dictionary[i] = 1

# 가장 많이 등장한 알파벳의 개수
max_value = max(count_dictionary.values())

# 가장 많이 등장한 알파벳이 두 개 이상이면 "?" 출력
if list(count_dictionary.values()).count(max_value) > 1:
    print("?")

# 가장 많이 등장한 알파벳이 한 개인 경우
else:
    print(max(count_dictionary, key=count_dictionary.get))


