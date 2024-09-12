from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))

visited = [[1] * N for _ in range(N)]
visitedRG = [[1] * N for _ in range(N)]

def bfs(i, j, alphabet):
    visited[i][j] = 0
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for r in range(4):
            nx = x + dx[r]
            ny = y + dy[r]            
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if visited[nx][ny] == 1 and arr[nx][ny] == alphabet:
                    q.append((nx, ny))
                    visited[nx][ny] = 0

def bfsRG(i, j, alphabet):
    visitedRG[i][j] = 0
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for r in range(4):
            nx = x + dx[r]
            ny = y + dy[r]            
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if alphabet == "R" or alphabet == "G":
                    if visitedRG[nx][ny] == 1 and (arr[nx][ny] == "R" or arr[nx][ny] == "G"):
                        q.append((nx, ny))
                        visitedRG[nx][ny] = 0
                else:
                    if visitedRG[nx][ny] == 1 and arr[nx][ny] == alphabet:
                        q.append((nx, ny))
                        visitedRG[nx][ny] = 0

answer = 0
answerRG = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            bfs(i, j, arr[i][j])            
            answer += 1
        if visitedRG[i][j] == 1:
            bfsRG(i, j, arr[i][j])
            answerRG += 1
print(answer, answerRG)


    
    