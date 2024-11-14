def solution(s):
    sList = []
    index = 0
    for i in s:
        if i != ' ':
            if index % 2 == 0: # 공백이 아니고 짝수번째
                sList.append(i.upper())
            else:
                sList.append(i.lower())
            index += 1
        else: # 공백이라면 인덱스 초기화
            index = 0    
            sList.append(" ")
    return ''.join(sList)