def solution(clothes):
    answer = 1
    map = dict()
    for c in clothes:
        if c[1] in map:
            map[c[1]].append(c[0])
        else:
            map[c[1]] = [c[0]]
    
    for key in map:
        answer *= len(map[key]) + 1
    
    return answer - 1