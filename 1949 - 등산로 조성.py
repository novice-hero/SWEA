def dfs(x, y, d, check):
  global answer
  
  if answer < d:
    answer = d

  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
      if mapInfo[nx][ny] < mapInfo[x][y]:
        visited[nx][ny] = 1
        dfs(nx, ny, d+1, check)
        visited[nx][ny] = 0

      elif mapInfo[nx][ny]-K < mapInfo[x][y] and not check:
        temp = mapInfo[nx][ny]
        mapInfo[nx][ny] = mapInfo[x][y] - 1
        check = True
        dfs(nx, ny, d+1, check)
        check = False
        mapInfo[nx][ny] = temp
  visited[x][y] = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]
T = int(input())
for tc in range(1, T+1):
  N, K = map(int, input().split())
  mapInfo = [list(map(int, input().split())) for _ in range(N)]
  answer = 0
  top = 0

  for i in range(N):
    top = max(top, max(mapInfo[i]))

  visited = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if mapInfo[i][j] == top:
        visited[i][j] = 1
        dfs(i, j, 1, False)
        visited[i][j] = 0
  
  print(f'#{tc} {answer}')
