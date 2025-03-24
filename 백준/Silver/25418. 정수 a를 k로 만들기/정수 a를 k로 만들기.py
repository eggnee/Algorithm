A, K = map(int, input().split())

dp = [0 for _ in range(K+1)]

for i in range(A+1, K+1):
    if i % 2 == 0 and i // 2 >= A:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[-1])

