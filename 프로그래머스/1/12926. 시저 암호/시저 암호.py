def solution(s, n):
    answer = ''
    for i in list(s):
        if i != " ":
            alphaNum = ord(i) + n
            if i.isupper():        
                if alphaNum > 90:
                    alphaNum -= 26
            else:
                if alphaNum > 122:
                    alphaNum -= 26
            answer += chr(alphaNum)
        else:
            answer += i
    return answer