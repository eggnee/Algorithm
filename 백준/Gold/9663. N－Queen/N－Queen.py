N = int(input())
case = [0] * N
result = 0

def checkPossible(usedNumber, position): # 지금까지 놓은 퀸 개수, 내가 놓을 퀸 열 위치
    for i in range(usedNumber): # 앞의 행들 퀸을 공격할 수 있는지 검사
        if abs((position - case[i]) / (usedNumber - i)) == 1 or position == case[i]:
            return False
    return True

def func(usedNumber): # 사용한 퀸 개수 1 ~ N
    global result
    
    if usedNumber == N:
        result += 1
        return
    
    for i in range(1, N+1):
        if checkPossible(usedNumber, i):
            case[usedNumber] = i # 인덱스는 0 ~ N-1
            func(usedNumber + 1)
            case[usedNumber] = 0


for i in range(1, N+1):
    case[0] = i
    func(1)
    case[0] = 0
    
print(result)