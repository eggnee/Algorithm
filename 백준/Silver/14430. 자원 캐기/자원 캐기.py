N, M = map(int, input().split())
target = []
for _ in range(N):
    target.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i != 0 and j != 0:
            dp[i][j] = max(dp[i-1][j] + target[i][j], dp[i][j-1] + target[i][j])
        elif i != 0:
            dp[i][j] = dp[i-1][j] + target[i][j]
        else:
            dp[i][j] = dp[i][j-1] + target[i][j]

print(dp[N-1][M-1])