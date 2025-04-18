#from collections import deque
import math

def solution(progresses, speeds):
    answers = []
    # 배포는 하루에 한 번
    # 각 배포마다 몇 개의 기능이 배포되는지
    # 먼저 들어간게 먼저 나가야 함 (최대 100번) 큐. 큐도 리스트 조회 O(1)?
    progresses.reverse()
    speeds.reverse()
    # 매번 
    while progresses:
        answer = 1
        progress = progresses.pop()
        speed = speeds.pop()
        count = math.ceil((100 - progress) / speed)
        
        while progresses:
            progress = progresses[-1]  
            speed = speeds[-1]
            if progress + (speed * count) >= 100:
                progresses.pop()
                speeds.pop()
                answer += 1
            else:
                break
                
        answers.append(answer)            
        
    
    return answers