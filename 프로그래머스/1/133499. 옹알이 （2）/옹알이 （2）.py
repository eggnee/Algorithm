# aya ye woo ma 조합만 발음할 수 있음, 연속 발음은 안됨

def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling:
        for j in word:            
            wordword = j + j
            if wordword in i:
                break
            else:                
                i = i.replace(j, "1")
        print(i)
        i = i.replace("1", "")
        if i == "":
            answer += 1
            
    return answer