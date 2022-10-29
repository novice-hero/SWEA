from itertools import permutations

T = int(input())
for t in range(T):
  n = list(input())
  n2 = int(''.join(n))
  nums = list(permutations(n, len(n)))
  flag = True

  if len(n) == 1:
    print(f'#{t+1} impossible')
    continue
  
  for s in nums:
    temp = int(''.join(s))
    if temp//n2 > 1 and temp%n2 == 0:
      flag = False
      print(f'#{t+1} possible')
      break
  
  if flag:
    print(f'#{t+1} impossible')