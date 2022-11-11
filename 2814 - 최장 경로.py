def dfs(start, cnt):
  global answer

  if answer < cnt:
    answer = cnt
  
  visited[start] = 1
  for next in graph[start]:
    if visited[next] == 0:
      visited[next] = 1
      dfs(next, cnt+1)
      visited[next] = 0
  visited[start] = 0

T = int(input())
for tc in range(1, T+1):
  N, M = map(int, input().split())
  graph = [[] for _ in range(11)]
  visited = [0 for _ in range(11)]
  answer = 0
  for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

  for i in range(N):
    dfs(i, 0)
  print(f'#{tc} {answer+1}')