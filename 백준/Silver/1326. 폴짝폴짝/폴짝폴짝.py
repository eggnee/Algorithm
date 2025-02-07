from collections import deque
n = int(input())
bridge = list(map(int, input().split()))
bridge = [0] + bridge
a, b = map(int, input().split())

distance = [-1] * (n+1)
distance[a] = 0

q = deque([a])

while q:
    now = q.popleft()
    
    for i in range(now, n + 1, bridge[now]):
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)
    
    for i in range(now, 0, -bridge[now]):
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)


if distance[b] != -1:
    print(distance[b])
else:
    print(-1)

