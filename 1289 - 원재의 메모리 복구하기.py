T = int(input())
for tc in range(1, T+1):
  mem = list(map(int, input()))
  cnt = 0
  while True:
    if 1 not in mem:
      print(f'#{tc} {cnt}')
      break
    idx = mem.index(1)
    for i in range(idx, len(mem)):
      if mem[i] == 1:
        mem[i] = 0
      else:
        mem[i] = 1
    cnt += 1