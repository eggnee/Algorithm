from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque([0 for _ in range(w)])
answer = 0

while trucks:
    truck = trucks.popleft()
    while True:
        answer += 1
        bridge.popleft()
        if truck + sum(bridge) <= L:
            bridge.append(truck)
            break
        bridge.append(0)

while sum(bridge) != 0 or bridge:
    answer += 1
    bridge.popleft()
    
print(answer)