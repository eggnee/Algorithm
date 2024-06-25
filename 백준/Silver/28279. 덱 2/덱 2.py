import sys
from collections import deque

N = int(input())
q = deque([])
for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))
    if len(cmd) == 2:
        if cmd[0] == 1:
            q.appendleft(cmd[1])
        elif cmd[0] == 2:
            q.append(cmd[1])
    else:
        if q:
            if cmd[0] == 3:
                print(q.popleft())
            elif cmd[0] == 4:
                print(q.pop())
            elif cmd[0] == 5:
                print(len(q))
            elif cmd[0] == 6:
                print(0)
            elif cmd[0] == 7:
                print(q[0])
            else:
                print(q[-1])
        else:
            if cmd[0] == 5:
                print(0)
            elif cmd[0] == 6:
                print(1)
            else:
                print(-1)