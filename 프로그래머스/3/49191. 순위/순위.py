from collections import deque

def solution(n, results):
    win = [[False] * (n + 1) for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    
    for a, b in results:
        graph[a].append(b)

    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        queue = deque([i])
        while queue:
            now = queue.popleft()
            for next_node in graph[now]:
                if not visited[next_node]:
                    win[i][next_node] = True
                    visited[next_node] = True
                    queue.append(next_node)

    answer = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if win[i][j] or win[j][i]:
                cnt += 1
        if cnt == n - 1:
            answer += 1

    return answer
