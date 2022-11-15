def dfs(cnt, total):
    if cnt == 3:
        answer.add(total)
        return
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, total+nums[i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    visited = [0]*len(nums)
    answer = set()
    dfs(0, 0)
    answer = list(answer)
    answer.sort(reverse=True)
    print(f'#{tc} {answer[4]}')
