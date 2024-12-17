def solution(n, lost, reserve):
    answer = 0
    newReserve =  list(set(reserve) - set(lost))
    newLost = list(set(lost) - set(reserve))
    for i in range(1, n+1):
        if i in newLost:
            if i-1 in newReserve:
                answer += 1
                reserve.remove(i-1)
            elif i+1 in newReserve:
                answer += 1
                newReserve.remove(i+1)
        else:
            answer += 1
    return answer