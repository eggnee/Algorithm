N = int(input())

maxDp = [0] * 3
minDp = [1e9] * 3

newMaxDp = [0] * 3
newMinDp = [0] * 3

numArr = list(map(int, input().split()))

for i in range(3):
    maxDp[i] = numArr[i]
    minDp[i] = numArr[i]

for _ in range(N-1):
    numArr = list(map(int, input().split()))
    for j in range(3):
        if j == 0:
            newMaxDp[j] = max(maxDp[j], maxDp[j+1]) + numArr[j]
            newMinDp[j] = min(minDp[j], minDp[j+1]) + numArr[j]
        elif j == 1:
            newMaxDp[j] = max(maxDp[j], maxDp[j+1], maxDp[j-1]) + numArr[j]
            newMinDp[j] = min(minDp[j], minDp[j+1], minDp[j-1]) + numArr[j]
        else:
            newMaxDp[j] = max(maxDp[j], maxDp[j-1]) + numArr[j]
            newMinDp[j] = min(minDp[j], minDp[j-1]) + numArr[j]
    
    maxDp = newMaxDp[:]
    minDp = newMinDp[:]


print(max(maxDp), min(minDp))                