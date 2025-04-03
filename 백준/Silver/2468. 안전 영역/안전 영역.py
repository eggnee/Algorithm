import sys
sys.setrecursionlimit(15000)

n = int(input())
arr = []
dx = [1, 0]
dy = [0, 1]
answer = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

def dfs(i, j, rain):
    if 0 <= i < n and 0 <= j < n:
        if visited[i][j] == False and arr[i][j] - rain > 0 :
            visited[i][j] = True
            dfs(i+1, j, rain)
            dfs(i-1, j, rain)
            dfs(i, j+1, rain)
            dfs(i, j-1, rain)
            return True

for rain in range(0, max(map(max, arr)) + 1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain):
                cnt += 1
    answer = max(answer, cnt)
            
print(answer)
