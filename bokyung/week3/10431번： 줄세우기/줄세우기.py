import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
  test = list(map(int, input().split()))
  count = 0
  # student 리스트에 첫번째 학생의 키를 넣어준다
  student = [test[1]]

  for i in range(2, 21):
    for j in student:
      # 리스트에 있는 학생의 키가 현재 학생의 키보다 크다면
      if j > test[i]:
        # 그 학생 앞에 현재 학생을 추가한다
        student.insert(student.index(j), test[i])
        # 현재 학생보다 큰 학생들의 길이를 추가한다
        count += len(student[student.index(j):])
        break
    else:
      # 현재 학생 보다 큰 학생이 없는 경우 맨 뒤에 추가한다
      student.append(test[i])

  print(test[0], count)
      