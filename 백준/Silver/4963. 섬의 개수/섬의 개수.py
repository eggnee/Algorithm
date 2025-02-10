import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

maps = []
case = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
w, h = map(int, input().split())

def dfs(i, j):
    if 0 <= i < h and 0 <= j < w:
        if maps[i][j] == 1:
            maps[i][j] = 0
            for c in case:
                dfs(i+c[0], j+c[1])
    

while True:
    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        maps.append(list(map(int, input().split())))
    
    num = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                num += 1
                dfs(i, j)
    print(num)
    
    w, h = map(int, input().split())
    maps = []


