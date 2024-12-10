# 당첨 가능한 최고 순위와 최저 순위를 배열에 담아서 반환하기

def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    num = 0
    zeroNum = 0
    
    for i in lottos:
        if i == 0:
            zeroNum += 1
        elif i in win_nums:
            num += 1
            
    return [rank[num + zeroNum], rank[num]]