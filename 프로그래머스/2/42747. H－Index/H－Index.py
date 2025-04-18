def solution(citations):
    # 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상 -> h의 최댓값
    answer = 0
    
    def check(h):
        count = 0
        for temp in citations:
            if temp >= h:
                count += 1
                if count >= h:
                    return True
        return False
        
    
    start = 0
    end = max(citations)
    
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
    
    
    return answer