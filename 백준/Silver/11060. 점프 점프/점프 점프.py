N = int(input())
arr = list(map(int, input().split()))
dp = [-1 for _ in range(N)]
dp[0] = 0

for i in range(0, N-1):
    for j in range(1, arr[i] + 1):
        if dp[i] != -1 and i + j < N:
            if dp[i+j] != -1:
                dp[i+j] = min(dp[i+j], dp[i] + 1)
            else:
                dp[i+j] = dp[i] + 1

print(dp[N-1])