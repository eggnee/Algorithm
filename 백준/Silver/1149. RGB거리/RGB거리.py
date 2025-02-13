# N개의 집 - 빨강, 초록, 파랑
# 비용의 최솟값 (각 집을 칠하는 비용이 다름)

# 조건 
# 1 != 2
# N-1 != N != N+1 (앞 뒤로 같은 색이면 안된다!)

# 빨강 초록 파랑 2차원 배열

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [[1e9] * 3 for _ in range(N)]

for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = cost[i][j]
        else:
            for k in range(3):
                if j != k:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + cost[i][j])

print(min(dp[N-1]))