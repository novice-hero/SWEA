def rowSumMax(arr):
  result = 0
  for i in range(len(arr)):
    result = max(result, sum(arr[i]))
  return result

def colSumMax(arr):
  tempList = [0]*len(arr)
  for i in range(len(arr)):
    for j in range(len(arr)):
      tempList[j] += arr[i][j]
  return max(tempList)

def diaSumMax(arr):
  tempList = [0,0]
  for i in range(len(arr)):
    for j in range(len(arr)):
      if i==j:
        tempList[0] += arr[i][j]
  for i in range(len(arr)-1, -1, -1):
    for j in range(len(arr)):
      if i==j:
        tempList[1] += arr[i][j]
  return max(tempList)

for _ in range(10):
  tc = int(input())
  arr = [list(map(int, input().split())) for _ in range(100)]
  print(f'#{tc} {max(rowSumMax(arr), colSumMax(arr), diaSumMax(arr))}')