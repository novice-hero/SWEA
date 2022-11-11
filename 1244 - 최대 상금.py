def dfs(cnt):
  global answer

  if not cnt:
    t = int(''.join(n))
    if answer < t:
      answer = t
    return

  for i in range(len(n)):
    for j in range(i+1, len(n)):
      n[i], n[j] = n[j], n[i]
      tempStr = ''.join(n)
      if visited.get((tempStr, cnt-1), 1):
        visited[(tempStr, cnt-1)] = 0
        dfs(cnt-1)
      n[i], n[j] = n[j], n[i]


T = int(input())
for tc in range(1, T+1):
  n, cnt = map(int, input().split())
  n = list(str(n))
  answer = 0
  visited = {}
  dfs(cnt)
  print(f'#{tc} {answer}')