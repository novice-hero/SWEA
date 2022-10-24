def check8():
  cnt = 0
  for i in range(8):
    for j in range(8):
      if board[i][j] == 'O':
        cnt += 1
  
  if cnt == 8:
    return True
  else:
    return False

def checkRook(x, y):
  cnt = 0

  if board[x].count('O') > 1:
    return False

  for i in range(8):
    if board[i][y] == 'O':
      cnt += 1
  if cnt > 1:
    return False
  
  return True

def checkXY():
  temp = []
  for i in range(8):
    for j in range(8):
      if board[i][j] == 'O':
        temp.append([i,j])
  return temp

n = int(input())
for i in range(n):
  board = [list(input()) for _ in range(8)]
  if check8():
    arr = checkXY()
    check = True
    for x,y in arr:
      if not checkRook(x,y):
        check = False
        print('#{0} no'.format(i+1))
        break
    if check:
      print('#{0} yes'.format(i+1))

  else:
    print('#{0} no'.format(i+1))