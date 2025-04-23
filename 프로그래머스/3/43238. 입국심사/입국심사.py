import math

def solution(n, times):
    number = math.ceil(n / len(times))
    start = number * min(times)
    end = number * max(times)
    answer = end
    
    def check(mid):
        count = 0
        for time in times:
            count += mid // time
        if count >= n:
            return True
        return False
    
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
        
    return answer