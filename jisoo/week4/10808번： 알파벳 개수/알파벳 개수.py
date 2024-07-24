s = input()

alphabet = [0] * 26

for w in s: 
  alphabet[ord(w) - 97] += 1

# print(' '.join(map(str, alphabet)))
print(*alphabet)