N = int(input())
arr = []

sum_num = 0
home_num = []


dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for _ in range(N):
    arr.append(list(map(int, input())))

def dfs(i, j, index):
    if 0 <= i < N and 0 <= j < N:
        if arr[i][j] == 1:
            home_num[index] += 1
            arr[i][j] = 0
            for d in dir:
                dfs(i+d[0], j+d[1], index)
            return True
    return False

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_num.append(0)            
            sum_num += 1
            dfs(i, j, len(home_num) - 1)
        

print(sum_num)
home_num.sort()
for home in home_num:
    print(home)
