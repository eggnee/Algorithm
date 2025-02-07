n = int(input())
chuList = list(map(int, input().split()))
chuList.sort()
result = [0, 0]
    
for i in chuList:
    newResult = [result[0] + i, result[1] + i]
    if newResult[0] - 1 <= result[1]:
        result = [result[0], newResult[1]]
    else:
        break
    
print(result[1] + 1)