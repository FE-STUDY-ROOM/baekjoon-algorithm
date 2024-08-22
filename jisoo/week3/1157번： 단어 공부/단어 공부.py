word = input().upper()
word_list = list(set(word))
lst = []

for w in word_list:
  cnt = word.count(w)
  lst.append(cnt)

if lst.count(max(lst)) >= 2:
  print('?')
else:
  print(word_list[lst.index(max(lst))])

