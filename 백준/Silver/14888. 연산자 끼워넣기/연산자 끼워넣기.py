import itertools

maxNum = float('-inf')
minNum = float('inf')

def cal(numList, operList, result):
    global maxNum, minNum
    
    if not numList:
        if maxNum < result:
            maxNum = result
        if minNum > result:
            minNum = result
        return
    
    newNumList = numList[:]
    oper = operList.pop(0)
    
    if oper == "+":
        result = result + newNumList.pop(0)
    elif oper == "-":
        result = result - newNumList.pop(0)
    elif oper == "*":
        result = result * newNumList.pop(0)
    else:
        if result < 0:
            result = -((-result) // newNumList.pop(0))
        else:
            result = result // newNumList.pop(0)
    
    #print(maxNum, minNum, result)
    #print(newNumList)
    
    cal(newNumList, operList, result)

N = int(input())
numList = list(map(int, input().split()))

operList = []
operInput = list(map(int, input().split()))
basicOper = ["+", "-", "*", "/"]

# 연산자 배열 생성
for i in range(4):
    for j in range(operInput.pop(0)):
        operList.append(basicOper[i])

operIterList = itertools.permutations(operList, N-1)

num = numList[0]
littleNumList = numList
littleNumList.pop(0)

for i in operIterList:
    #print(i)
    cal(littleNumList, list(i), num)

print(maxNum)
print(minNum)

