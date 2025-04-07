T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[0] * n for _ in range(2)]
    arr = []

    for _ in range(2):
        arr.append(list(map(int, input().split())))

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    
    if n > 1:
        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

    
    for j in range(2, n):
        for i in range(2):
            dp[i][j] = max(max(dp[0][j-2], dp[1][j-2]) + arr[i][j], dp[abs(i-1)][j-1] + arr[i][j])

    print(max(max(row) for row in dp))
        
    