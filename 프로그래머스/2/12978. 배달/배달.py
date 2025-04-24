import heapq


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    
    for node in road:
        graph[node[0]].append((node[1], node[2]))
        graph[node[1]].append((node[0], node[2]))
    
    
    distance = [int(1e9)] * (N + 1)
    distance[1] = 0
    
    q = []
    heapq.heappush(q, (0, 1))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            new_dist = dist + cost
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))                
        
    distance = distance[1:]        
    
    return sum(1 for temp in distance if temp <= K)