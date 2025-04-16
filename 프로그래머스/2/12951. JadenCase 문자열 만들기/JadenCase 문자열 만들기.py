def solution(s):
    flag = True    
    answer = ''
    for alpha in s:
        if alpha == " ":                  
            flag = True
            answer += alpha  
        else:
            if flag:
                answer += alpha.upper()
                flag = False
            else:
                answer += alpha.lower()
                    
    return answer