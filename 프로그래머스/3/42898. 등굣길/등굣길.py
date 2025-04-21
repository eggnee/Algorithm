def solution(m, n, puddles):
    dp = [[0] * n for _ in range(m)]
    
    for puddle in puddles:
        if puddle:  
            dp[puddle[0]-1][puddle[1]-1] = -1
    
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if i != 0 or j != 0:
                if dp[i][j] != -1:
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:    
                        if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                            dp[i][j] = -1
                            continue
                        
                        if dp[i-1][j] == -1:
                            dp[i][j] = dp[i][j-1]
                        elif dp[i][j-1] == -1:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    if dp[-1][-1] == -1:
        return 0
    return dp[-1][-1] % 1000000007