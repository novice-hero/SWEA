s = 'abcdefghijklmnopqrstuvwxyz'
alphabet = {}
for i in range(len(s)):
  alphabet[i] = s[i]

n = int(input())
for i in range(n):
  temp = input()
  cnt = 0
  for j in range(len(temp)):
    if temp[j] == alphabet[j]:
      cnt += 1
    else:
      break

  print('#{0} {1}'.format(i+1, cnt))