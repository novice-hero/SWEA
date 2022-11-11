def dfs(idx, score, kcal):
  global answer

  if kcal > L:
    return
  if answer < score:
    answer = score
  if idx == N:
    return
  
  dfs(idx+1, score+burger[idx][0], kcal+burger[idx][1])
  dfs(idx+1, score, kcal)

T = int(input())
for tc in range(T):
  N, L = map(int, input().split())
  burger = [list(map(int, input().split())) for _ in range(N)]
  answer = 0
  dfs(0,0,0)

  print(f'#{tc+1} {answer}')