N, M = map(int, input().split())
answer = 600
space = []
dir = [-1, 0, 1]

for _ in range(N):
    space.append(list(map(int, input().split())))

def dfs(row, column, pre_dir, price):
    global answer
    if row == N:
        answer = min(answer, price)
        return
    if 0 <= row < N and 0 <= column < M:
        for d in range(3):
            if d != pre_dir:
                dfs(row + 1, column + dir[d], d, price + space[row][column])

for column in range(M):
    dfs(0, column, -1, 0)

print(answer)