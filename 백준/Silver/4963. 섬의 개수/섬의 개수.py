import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

route = [[0, 1], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, 0], [-1, -1], [0, -1]]

def dfs(visited, i, j):
    if visited[i][j] == 0 and arr[i][j] == 1:
        visited[i][j] = 1
        for k in route:
            if 0 <= i+k[0] and i+k[0] < h and 0 <= j+k[1] and j+k[1] < w:
                dfs(visited, i+k[0], j+k[1])
            
            
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    answer = 0
    visited = [[0] * w for _ in range(h)]
    
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and arr[i][j] == 1:
                answer += 1
                dfs(visited, i, j)
    print(answer)



    