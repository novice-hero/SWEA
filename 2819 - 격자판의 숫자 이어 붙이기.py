def dfs(a, b, s):
  if len(s) == 7:
    count.add(s)
    return
  
  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    if 0<=nx<4 and 0<=ny<4:
      dfs(nx, ny, s+str(board[nx][ny]))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
T = int(input())
for t in range(T):
  board = [list(map(int, input().split())) for _ in range(4)]
  count = set()
  s = ''
  for i in range(4):
    for j in range(4):
      dfs(i, j, s)

  print(f'#{t+1} {len(count)}')