from collections import deque

T = int(input())
for _ in range(T):
    front = deque()
    back = deque()
    L = input()
    for i in L:
        if i == '<':
            if front:
                back.appendleft(front.pop())
        elif i == '>':
            if back:
                front.append(back.popleft())
        elif i == '-':
            if front:
                front.pop()
        else:
            front.append(i)

    print(''.join(front) + ''.join(back))