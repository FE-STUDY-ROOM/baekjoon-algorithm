import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
  tmp = sys.stdin.readline().strip().split()

  if len(tmp) == 1:
    if tmp[0] == 'all':
      S = set([i for i in range(1, 21)])
    else:
      S = set()
  else:
    fn, x = tmp[0], tmp[1]
    x = int(x)

    if fn == 'add':
      S.add(x)
    elif fn == 'remove':
      S.discard(x)
    elif fn == 'check':
      print(1 if x in S else 0)
    elif fn == 'toggle':
      if x in S:
        S.discard(x)
      else:
        S.add(x)