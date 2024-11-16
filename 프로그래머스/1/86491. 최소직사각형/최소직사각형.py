def solution(sizes):
    return max([max(j) for j in sizes]) * max([min(j) for j in sizes])
    