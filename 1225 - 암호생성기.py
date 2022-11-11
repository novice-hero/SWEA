for tc in range(1, 11):
  n = int(input())
  data = list(map(int, input().split()))
  check = True

  while check:
    for i in range(1, 6):
      if data[0]-i > 0:
        data[0] = data[0]-i
        data = data[1:]+data[:1]
      else:
        data[0] = 0
        data = data[1:]+data[:1]
        check = False
        break
  
  print('#{} {} {} {} {} {} {} {} {}'.format(tc, *data))