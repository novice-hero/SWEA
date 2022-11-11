T = int(input())
for tc in range(1, T+1):
  N = int(input())
  score = list(map(int, input().split()))
  visited = [0]*(sum(score)+1)
  visited[0] = 1

  for i in score:
    for j in range(len(visited)-i, -1, -1):
      if visited[j]:
        visited[i+j] = 1
  
  print(f'#{tc} {sum(visited)}')