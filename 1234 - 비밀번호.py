for tc in range(1, 11):
  n, numstr = map(int, input().split())
  numstr = list(str(numstr))
  stack = []
  for n in numstr:
    if len(stack) == 0:
      stack.append(n)
    elif stack[-1] == n:
      stack.pop()
    else:
      stack.append(n)
  answer = ''.join(stack)
  answer = int(answer)
  print(f'#{tc} {answer}')