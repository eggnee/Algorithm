def solution(clothes):
    answer = 1
    map = dict()
    for _, t in clothes:
        if t in map:
            map[t] += 1
        else:
            map[t] = 2
    
    for value in map.values():
        answer *= value
    
    return answer - 1