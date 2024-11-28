# 매일 "명예의 전당" 최하위 점수를 발표
# sort 해서 인덱스 2 리턴


def solution(k, score):
    answer = []
    for i in range(len((score))):
        nowScore = score[:i+1]
        nowScore.sort(reverse=True)
        if len(nowScore) >= k:
            answer.append(nowScore[k-1])
        else:
            answer.append(nowScore[-1])            
    return answer