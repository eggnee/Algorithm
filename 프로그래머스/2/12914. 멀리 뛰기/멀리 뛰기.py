def solution(n):
    # 1칸이나 2칸
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    if n >= 2:
        dp[2] = 2   
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1] % 1234567