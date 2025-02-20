moveCase = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 동쪽(0) - (0, 1) 서쪽(2) - (0, -1) 남쪽(1) - (1, 0) 북쪽(3) - (-1, 0) 

def func():
    M, n = map(int, input().split())
    target = (0, M)
    nowLoc = (M, 0)
    nowDir = 0
    
    for _ in range(n):
        cmd = list(input().split())
        if cmd[0] == 'MOVE':
            nowLoc = (nowLoc[0] + int(cmd[1]) * moveCase[nowDir][0], nowLoc[1] + int(cmd[1]) * moveCase[nowDir][1])
            if nowLoc[0] < 0 or nowLoc[0] > M or nowLoc[1] < 0 or nowLoc[1] > M:
                print(-1)
                return
        else:
            if int(cmd[1]) == 0:
                nowDir = (nowDir + 3) % 4
            else:
                nowDir = (nowDir + 1) % 4
            
    print(nowLoc[1], M - nowLoc[0])

func()