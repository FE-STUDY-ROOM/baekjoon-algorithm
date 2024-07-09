import sys
from collections import deque
input = sys.stdin.readline

# 입력, 카드 생성
n = int(input())
cards = deque([i for i in range(1,n+1)])

# 마지막 카드가 남을 때까지 반복
while len(cards) > 1:
    # 제일 위에 있는 카드를 버린다
    cards.popleft()
    # 그 다음, 제일 위에 있는 카드를
    card = cards.popleft()
    # 제일 아래에 있는 카드 밑으로 옮긴다.
    cards.append(card)
    
# 남게 되는 카드의 번호 출력
print(cards[0])