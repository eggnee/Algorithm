def solution(array, commands):
    answer = []
    for cmd in commands:
        newArr = array[cmd[0]-1 : cmd[1]]
        newArr.sort()
        answer.append(newArr[cmd[2]-1])    
    return answer