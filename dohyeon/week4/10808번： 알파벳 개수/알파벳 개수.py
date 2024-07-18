import sys
s = sys.stdin.readline().rstrip()

# 알파벳 리스트
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# 알파벳 리스트를 돌면서 문자열에서 해당 알파벳이 몇개 있는지 출력
for i in alphabet:
  print(s.count(i), end=" ")


