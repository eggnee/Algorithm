import heapq

def solution(scoville, K): 
    answer = 0    
    
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        heapq.heappush(scoville, mix)
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    
    return answer