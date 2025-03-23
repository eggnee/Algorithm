def check(stones, num, k):
    zero_count = 0  # 연속된 0의 개수
    
    for stone in stones:
        if stone < num:  # num보다 작으면 0이 되는 것과 같음
            zero_count += 1
            if zero_count >= k:  # k개 연속되면 실패
                return False
        else:
            zero_count = 0  # 연속된 0이 끊김
    return True


def solution(stones, k):
    start, end = 1, max(stones)
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        if check(stones, mid, k):  
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return answer
