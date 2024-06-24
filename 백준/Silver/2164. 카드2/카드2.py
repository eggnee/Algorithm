from collections import deque

cardQueue = deque([])
N = int(input())
for i in range(1, N+1):
    cardQueue.append(i)

while len(cardQueue) != 1:
    cardQueue.popleft()
    cardQueue.append(cardQueue.popleft())

print(cardQueue.pop())