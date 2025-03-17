arr = []
for _ in range(19):
    arr.append(list(map(int, input().split())))

dArr = [(0, 1), (1, 1), (1, 0), (1, -1)]

def dfs(i, j, stone, d):
    num = 1
    answer = [i, j]
    while True:
        i += dArr[d][0]
        j += dArr[d][1]
        if i < 0 or i >= 19 or j < 0 or j >= 19 or arr[i][j] != stone:
            if num == 5:
                print(stone)
                print(answer[0]+1, answer[1]+1)
                return True
            else:
                return False
        num += 1
        if answer[1] > j:
            answer = [i, j]

def program():
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                for d in range(4):
                    if i-dArr[d][0] >= 0 and 0 <= j-dArr[d][1] < 19:
                        if arr[i-dArr[d][0]][j-dArr[d][1]] != arr[i][j]:
                            if dfs(i, j, arr[i][j], d):
                                return
                    else:
                        if dfs(i, j, arr[i][j], d):
                            return
    print(0)

program()