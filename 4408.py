T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0]*401
    for _ in range(N):
        now, re = map(int, input().split())
        if not now == re:
            for i in range((min(now, re)+1)//2, (max(now, re)+1)//2+1):
                visited[i] += 1
    print(f'#{tc} {max(visited)}')
