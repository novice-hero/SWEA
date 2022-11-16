def dfs(cnt):
    if cnt == 1:
        if ''.join(N)[0] != '0':
            answer.add(''.join(N))
        return

    for i in range(len(N)):
        for j in range(i, len(N)):
            if not visited[i] and not visited[j]:
                visited[i], visited[j] = 1, 1
                N[i], N[j] = N[j], N[i]
                dfs(cnt+1)
                N[i], N[j] = N[j], N[i]
                visited[i], visited[j] = 0, 0


T = int(input())
for tc in range(1, T+1):
    N = list(input())
    visited = [0]*len(N)
    answer = set()
    answer.add(''.join(N))
    dfs(0)
    answer = list(answer)

    print(f'#{tc} {min(answer)} {max(answer)}')