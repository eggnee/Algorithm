from collections import deque

N, K = map(int, input().split())
people = deque([])
answer = []
for i in range(1, N+1):
    people.append(str(i))

while people:
    for _ in range(K-1):
        people.append(people.popleft())
    answer.append(people.popleft())
    
print("<" + ", ".join(answer) + ">")