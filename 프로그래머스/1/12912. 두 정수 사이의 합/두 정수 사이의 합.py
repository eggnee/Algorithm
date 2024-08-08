def solution(a, b):
    return sum(i for i in range(min(a, b), max(a+1, b+1)))