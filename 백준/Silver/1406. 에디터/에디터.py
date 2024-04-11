import sys
from collections import deque

front = deque(input())
m = int(input())
end = deque()

for _ in range(m):
    cmd = sys.stdin.readline().strip()
    if cmd == "L":
        if len(front) > 0:
            end.insert(0, front.pop())
    elif cmd == "D":
        if len(end) > 0:
            front.append(end.popleft())
    elif cmd == "B":
        if len(front) > 0:
            front.pop()
    else:
        cmdList = list(cmd.split())
        front.append(cmdList[1])

print(''.join(front) + ''.join(end))