N, M = map(int, input().split())
arr = [0] * M
isUsed = [0] * (N + 1)
num = 0

def fun(i):
    if i == M:
        for a in arr:
            print(a, end = " ")
        print()
        return
    
    for j in range(1, N + 1):
        if isUsed[j] == 0:
            arr[i] = j
            isUsed[j] = 1
            fun(i+1)
            isUsed[j] = 0
    

for i in range(1, N+1):
    isUsed[i] = 1
    arr[0] = i
    fun(1)
    isUsed[i] = 0
    