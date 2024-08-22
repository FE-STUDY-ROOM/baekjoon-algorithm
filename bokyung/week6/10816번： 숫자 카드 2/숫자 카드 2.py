import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
card_list = list(map(int, input().split()))
card_dict = {}

for i in card_list:
    if card_dict.get(i, -1) == -1:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

m = int(input())
check_list = list(map(int, input().split()))

for i in check_list:
    print(card_dict.get(i, 0), end=' ')