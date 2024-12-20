def toAlpha(alpha):
    return chr((alpha - 97) % 26 + 97)    

def solution(s, skip, index):
    answer = ''
    for i in s:
        alpha = ord(i)
        for _ in range(index):
            alpha += 1
            while toAlpha(alpha) in skip:
                alpha += 1
        answer += toAlpha(alpha)            
    return answer

      