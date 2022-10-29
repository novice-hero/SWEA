T = int(input())
for t in range(T):
  n = int(input())
  farm = [list(map(int, input())) for _ in range(n)]
  result = 0
  mid = (n-1)//2
  for i in range(n):
    if i <= mid:
      result += sum(farm[i][mid-i:mid+1+i])
    else:
      result += sum(farm[i][i-mid:mid-i])
  
  print(f'#{t+1} {result}')