n, k = map(int, input().split())

dp = [0] * (k + 1)
dpStock = [[] for _ in range(k+1)]
W = [0]
V = [0]

for _ in range(n):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)

for i in range(k + 1):
    for j in range(n + 1):
        if i - W[j] >= 0 and i != i - W[j]:
            if j not in dpStock[i - W[j]]:
                if dp[i] < V[j] + dp[i-W[j]]:
                    dpStock[i] = dpStock[i-W[j]] + [j]
                    dp[i] = max(dp[i], V[j] + dp[i-W[j]])
     
print(max(dp))