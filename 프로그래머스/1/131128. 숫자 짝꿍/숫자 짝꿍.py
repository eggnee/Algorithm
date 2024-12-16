# 공통 숫자 넣는 배열에 추가
# 내림차순 정렬

def solution(X, Y):
    common = ""
    for i in range(10):
        num = min(X.count(str(i)), Y.count(str(i)))
        if num != 0:
            for _ in range(num):
                common += str(i)
                
    common = list(common)
    if not common:
        return str(-1)
    
    common.sort(reverse=True)
    answer = "".join(common)
    
    if answer.replace("0", "") == "":
        return "0"
    return answer