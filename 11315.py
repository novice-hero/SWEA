def check():
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if game[i][j] == 'o':
                for d in range(4):
                    nx = i
                    ny = j
                    cnt = 0
                    while 0 <= nx < N and 0 <= ny < N and game[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[d]
                        ny += dy[d]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    game = [input() for _ in range(N)]
    print(f'#{tc} {check()}')