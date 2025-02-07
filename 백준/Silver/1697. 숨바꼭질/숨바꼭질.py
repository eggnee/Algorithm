from collections import deque

def bfs(x):
    global result
    q = deque()
    q.append(x)
    visited = [0] * 100001
    visited[x] = 1
    
    while q:
        x = q.popleft()
        if x == k:
            result = visited[x] - 1
            return
        tmp = [] # 연결 노드 담을 리스트
        tmp.extend([x-1, x+1, 2 * x])
        for v in tmp:
            if 0 <= v <= 100000:
                if not visited[v]:
                    visited[v] = visited[x] + 1
                    q.append(v)
        tmp = []
    

n, k = map(int, input().split())
result = 0
bfs(n)
print(result)

