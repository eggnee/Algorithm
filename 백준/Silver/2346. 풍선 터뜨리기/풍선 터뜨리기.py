import sys
from collections import deque

N = int(input())
q = deque([i for i in range(1, N+1)])
paperList = list(map(int, sys.stdin.readline().split()))

def breakBalloon(num):
    if num > 0:
        for _ in range(num-1):
            q.append(q.popleft())
    else:
        num = -num
        for _ in range(num):
            q.appendleft(q.pop())
    print(q[0], end = " ")
    return q.popleft()

print(1, end = " ")
answer = breakBalloon(paperList[q.popleft() - 1])
while q:
    answer = breakBalloon(paperList[answer - 1])
    
