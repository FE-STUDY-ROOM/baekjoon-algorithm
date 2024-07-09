import sys

def input():
  return sys.stdin.readline().rstrip()

# 666 ~ 5666 
# 6660부터는 6661, 6662 이런식으로 된다..... 이거 개수를 어떻게 세지..? 모르겠습니다

# 모든 경우의 수를 다 구한다

n = int(input())

# 우리는 666이 들어가는 값을 찾아야 하고, 그 첫 값은 666
target = 666
count = 0

while True:
  # 타겟 값에 666이 있는지 확인한다
  if '666' in str(target):
    # 666이 있으면 count를 1 추가한다 => 666이 들어가는 숫자만 찾아야 하기 때문에 있는 경우에만 count 추가
    count += 1
    # count와 n이 일치하면 우리가 원하는 순번의 숫자라는 것
    if count == n:
      break
  # 계속 1씩 더해간다
  target += 1

# 우리가 구한 값을 출력한다
print(target)