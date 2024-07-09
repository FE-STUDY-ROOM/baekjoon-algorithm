 # 입력을 정수로 변환
import sys
n = int(sys.stdin.readline().strip()) 

# 카드 덱 만들기
cards = list(range(1, n+1))

# 카드가 한 장 남을 때까지 반복
while len(cards) > 1:
    # 제일 위에 있는 카드를 버림
    cards.pop(0) 
    # 그 다음 제일 위에 있는 카드를 맨 밑으로 옮김
    cards.append(cards.pop(0)) 

print(cards[0])  # 마지막 남은 카드 출력