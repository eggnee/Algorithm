from collections import deque

def solution(n, edge):
    visited = [-1 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    
    for temp in edge:
        graph[temp[0]].append(temp[1])
        graph[temp[1]].append(temp[0])
        
    queue = deque([(1, 0)])
    
    while queue:
        v, count = queue.popleft()
        if visited[v] == -1:
            visited[v] = count
            
            for node in graph[v]:
                queue.append((node, count + 1))
    
    max_path = max(visited)
    return visited.count(max_path)