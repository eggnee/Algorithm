N, S = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

def dfs(index, sumValue):
    global result
    
    if index >= N:
        return
    
    sumValue += nums[index]
    
    if sumValue == S:
        result += 1
    
    for i in range(index + 1, N + 1):
        dfs(i, sumValue)


for i in range(N):   
    dfs(i, 0)

print(result)