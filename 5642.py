T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[0]
    for i in range(N-1):
        if arr[i] >= 0 and (arr[i] + arr[i+1]) >= 0:
            arr[i+1] += arr[i]
        if max_value < arr[i+1]:
            max_value = arr[i+1]
    print(f'#{tc} {max_value}')