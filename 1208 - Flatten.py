for tc in range(1, 11):
  dump = int(input())
  box = list(map(int, input().split()))
  
  while dump > 0:
    box_max = max(box)
    box_min = min(box)
    maxIdx = box.index(box_max)
    minIdx = box.index(box_min)
    box[maxIdx] -= 1
    box[minIdx] += 1
    dump -= 1

  print(f'#{tc} {max(box)-min(box)}')
