def solution(people, limit):
    # 2명씩 밖에 못 탐
    # [80 70 50 50] -> 젤 많이 채워서 보내야 한다!
    # [70 70 20 20] [20 20 70 70]
    
    people.sort(reverse=True)
    
    answer = 0
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if people[start] + people[end] <= limit:
            end -= 1        
        answer += 1
        start += 1 
    
            
    return answer