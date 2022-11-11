def dfs(n):
  global answer

  if n == N:
    answer += 1
    return
  
  for j in range(N):
    if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0:
      v1[j], v2[n+j], v3[n-j] = 1, 1, 1
      dfs(n+1)
      v1[j], v2[n+j], v3[n-j] = 0, 0, 0

T = int(input())
for tc in range(1, T+1):
  N = int(input())
  answer = 0
  v1 = [0]*(2*N) # 행 확인
  v2 = [0]*(2*N) # / 확인
  v3 = [0]*(2*N) # \ 확인
  dfs(0)
  print(f'#{tc} {answer}')