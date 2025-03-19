import math

N = int(input())
M = int(input())
XList = list(map(int, input().split()))

answer = max(XList[0], N - XList[-1])
for i in range(1, M):
    answer = max(answer, math.ceil((XList[i] - XList[i-1]) / 2))

print(answer)