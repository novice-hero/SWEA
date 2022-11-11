def dfs(idx, s):
  global answer
  if s > K:
    return
  if s == K:
    answer += 1
    return
  for i in range(idx, N):
    dfs(i+1, s+A[i])

T = int(input())
for tc in range(1, T+1):
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  answer = 0
  dfs(0, 0)
  print(f'#{tc} {answer}')