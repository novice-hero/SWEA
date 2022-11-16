T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    visited = [0]*N
    answer = []
    commit = list(map(int, input().split()))
    for c in commit:
        visited[c-1] = 1
    for i in range(len(visited)):
        if not visited[i]:
            answer.append(i+1)
    print(f'#{tc}', end=' ')
    print(*answer)