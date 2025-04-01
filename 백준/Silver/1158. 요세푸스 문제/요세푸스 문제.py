from collections import deque

N, K = map(int, input().split())
arr = deque([i for i in range(1, N+1)])

print("<", end = "")
while len(arr) > 1:
    for _ in range(K-1):
        arr.append(arr.popleft())
    print(arr.popleft(), end = ", ")

print(arr.popleft(), end = "")
print(">")

