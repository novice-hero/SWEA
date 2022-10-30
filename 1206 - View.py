for t in range(10):
  N = int(input())
  height = list(map(int, input().split()))
  result = 0

  for i in range(2, len(height)-2):
    if height[i] == 0:
      continue
    if height[i] > max(height[i-2:i]) and height[i] > max(height[i+1:i+3]):
      result += height[i] - max(height[i-2],height[i-1],height[i+1],height[i+2])
    else:
      continue

  print(f'#{t+1} {result}')