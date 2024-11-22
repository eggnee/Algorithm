import itertools 

def solution(numbers):
    combi = itertools.combinations(numbers, 2)
    return sorted(list(set([sum(i) for i in combi])))