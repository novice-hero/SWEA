def dfs(x, y):
  global answer, start

  if x==n-1 and y==n-1:
    if answer > start:
      answer = start
    return
  elif answer < start:
    return

  for i in range(2):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<n:
      start += graph[nx][ny]
      dfs(nx, ny)
      start -= graph[nx][ny]

dx = [0,1]
dy = [1,0]
T = int(input())
for t in range(T):
  n = int(input())
  graph = [list(map(int, input().split())) for _ in range(n)]
  answer = 1e9
  start = graph[0][0]
  dfs(0,0)

  print(f'#{t+1} {answer}')