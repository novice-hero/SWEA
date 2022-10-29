def dfs(cur, temp):
  global result
  if temp < result:
    if 0 not in visited[1:]:
      result = min(result, temp+area[cur][0])
      return
    for i in range(1, n):
      if area[cur][i] != 0 and visited[i] == 0:
        visited[i] = 1
        dfs(i, temp+area[cur][i])
        visited[i] = 0

T = int(input())
for t in range(T):
  n = int(input())
  area = [list(map(int, input().split())) for _ in range(n)]
  result = 1e9
  for i in range(1, n):
    visited = [0]*n
    visited[i] = 1
    dfs(i, area[0][i])
  print(f'#{t+1} {result}')