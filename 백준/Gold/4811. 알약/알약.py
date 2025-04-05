dp = [0 for _ in range(31)]
dp[0] = 1

for i in range(1, 31):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j] 

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N])