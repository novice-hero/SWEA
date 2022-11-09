from collections import deque
def bfs(s):
  global answer
  q = deque()
  q.append(s)
  visited[s] = 1

  while q:
    now = q.popleft()
    for next in network[now]:
      if not visited[next]:
        visited[next] = visited[now] + 1
        q.append(next)

for tc in range(1, 11):
  length, start = map(int, input().split())
  inp = list(map(int, input().split()))
  network = [[] for _ in range(101)]
  visited = [0 for _ in range(101)]
  for i in range(length):
    if i%2==0:
      network[inp[i]].append(inp[i+1])
  
  bfs(start)
  
  max_cnt = max(visited)
  answer = []
  for i in range(len(visited)):
    if max_cnt == visited[i]:
      answer.append(i)
  print(f'#{tc} {max(answer)}')