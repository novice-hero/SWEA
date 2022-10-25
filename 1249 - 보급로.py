from collections import deque

def bfs():
  global num
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  visited = [[1e9]*num for _ in range(num)]

  q = deque()
  q.append([0,0])
  visited[0][0] = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<num and 0<=ny<num:
        if visited[x][y]+mapInfo[nx][ny] < visited[nx][ny]:
          visited[nx][ny] = visited[x][y]+mapInfo[nx][ny]
          q.append([nx,ny])

  return visited[-1][-1]

n = int(input())
for i in range(n):
  num = int(input())
  mapInfo = [list(map(int, input())) for _ in range(num)]
  
  print(f'#{i+1} {bfs()}')