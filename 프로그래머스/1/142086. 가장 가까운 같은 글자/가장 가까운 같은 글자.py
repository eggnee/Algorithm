def solution(s):
    answer = []
    for i in range(len(s)):
        newS = s[0:i]
        index = newS.rfind(s[i])
        if index == -1:
            answer.append(index)
        else:
            answer.append(i-index)
    return answer