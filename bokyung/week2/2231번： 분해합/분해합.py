import sys, itertools

def input():
  return sys.stdin.readline().rstrip()

# 가장 작은 생성자 구하기
# 주어진 숫자의 자릿수를 확인한다
# 주어진 숫자 - 자릿수*(1~9) 값이 자릿수를 조합한 숫자와 일치하는지 확인한다
# 일치하면 리스트에 추가하고, 리스트에서 가장 작은 값을 리턴한다

n = input()

# 생성자 값을 저장할 리스트
# target_list = []

# 순서가 필요하기 때문에 중복순열을 이용하여 각 자릿수를 구한다
# 그냥 하면 런타임 에러가 발생한다 => 숫자 범위를 줄이고 싶은데 어떻게 하면 좋을 지 모르겠다. 어차피 n에서 작아질 수 있는 크기는 제한적이기 때문에 범위를 줄이고 싶은데 모르겠다.

# for i in itertools.product(range(1,10), repeat=len(n)):
#   target = int(''.join(map(str, list(i))))

#   if int(n) > target and int(n) - sum(i) == target:
#     target_list.append(target)

# if len(target_list) == 0:
#   print(0)
# else:
#   print(min(target_list))


for i in range(1, int(n)+1):
  # i의 각 자리수를 더한다(생성자)   
  num = sum((map(int, str(i))))
  # 분해합 = 생성자(i) + 각 자릿수의 합(num)
  num_sum = i + num
  # 지금 구한 분해합이 n과 일치하면 생성자
  # n이 1부터 시작하기 때문에 제일 먼저 나온 값이 최솟값 => 나오면 break
  if num_sum == int(n):
    print(i)
    break
else:
  # for문을 종료할 때까지 break가 되지 않으면(생성자가 없으면) 0 출력
  print(0)

# 굳이 순열을 이용할 필요가 없었다.....