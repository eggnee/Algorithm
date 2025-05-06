import sys

n = int(input())
grape = [0]

for _ in range(n):
    grape.append(int(sys.stdin.readline()))

dp = [0 for _ in range(n + 1)]
dp[1] = grape[1]

if n >= 2:
    dp[2] = grape[1] + grape[2]

if n >= 3:
    dp[3] = max(grape[1], grape[2]) + grape[3]

for i in range(4, n + 1):
    dp[i] = max(dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i], dp[i-4] + grape[i-1] + grape[i])

print(max(dp))