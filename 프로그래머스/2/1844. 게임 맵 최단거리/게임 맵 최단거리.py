from collections import deque


def solution(maps):
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    queue = deque([])
    queue.append((0, 0, 1))
    
    while queue:
        i, j, dis = queue.popleft()
        if 0 <= i < len(maps) and 0 <= j < len(maps[0]):
            if maps[i][j] == 1:
                maps[i][j] = dis
                if i + 1 == len(maps) and j + 1 == len(maps[0]):   
                    return maps[i][j]
                for d in direction:
                    queue.append((i + d[0], j + d[1], maps[i][j] + 1))
    
    
    return -1