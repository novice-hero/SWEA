def sol(n,m):
  global N, answer
  if m == 0:
    return 1
  else:
    return n * sol(n, m-1)

for _ in range(10):
  tc = int(input())
  N, M = map(int, input().split())
  print(f'#{tc} {sol(N,M)}')
