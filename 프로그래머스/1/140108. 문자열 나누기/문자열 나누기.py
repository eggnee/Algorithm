# x

def solution(s):
    answer = 0
    first = True
    for i in s:
        if first:
            x = i
            xNum = 1
            notXNum = 0
            first = False
        else:
            if i == x:
                xNum += 1
            else:
                notXNum += 1
            if xNum == notXNum:
                answer += 1
                first = True   
    if xNum != notXNum:
        answer += 1
    return answer