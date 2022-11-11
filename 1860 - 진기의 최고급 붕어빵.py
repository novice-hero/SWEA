T = int(input())
for tc in range(1, T+1):
  N, M, K = map(int, input().split())
  customer = list(map(int, input().split()))
  customer.sort()

  bread = 0
  flag = True
  max_time = max(customer)
  for i in range(max_time+1):
    if i%M==0 and i!=0:
      bread += K
    if i==customer[0]:
      if bread == 0:
        print(f'#{tc} Impossible')
        flag = False
        break
      else:
        customer.pop(0)
        bread -= 1
  
  if flag:
    print(f'#{tc} Possible')