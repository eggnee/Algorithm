# 1점 ~ k점의 사과를 한 상자에 m개씩 포장
# 한 상자의 가격은 가장 낮은 점수 p * m (개수) -> 최대 이익 리턴

def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        for i in range(m-1):
            score.pop()
        answer += score.pop() * m
    return answer