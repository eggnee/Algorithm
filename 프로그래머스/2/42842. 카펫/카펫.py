def solution(brown, yellow):
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_height = i
            yellow_width = yellow // i
            
            if yellow_width * 2 + yellow_height * 2 + 4 == brown:
                answer = [yellow_height + 2, yellow_width + 2]
                break
    
    return sorted(answer, reverse=True)