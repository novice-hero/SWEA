T = int(input())
for tc in range(1, T+1):
    n, d = map(int, input().split())
    answer = 0
    if n%(2*d + 1) == 0:
        answer = n//(2*d + 1)
    else:
        answer = n//(2*d + 1) + 1
    print(f'#{tc} {answer}')
