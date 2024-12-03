# 12345 12345 ...
# 21 23 24 25 21 23 24 25 ...
# 33 11 22 44 55 33 11 ...

def solution(answers):
    supos = [[1, 2, 3, 4, 5], 
               [2, 1, 2, 3, 2, 4, 2, 5], 
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
              ]
    
    scores = []
    for i in range(3):
        score = 0
        k = 0
        for j in range(len(answers)):   
            if answers[j] == supos[i][k]:
                score += 1
            k += 1
            if k == len(supos[i]):
                k = 0    
        scores.append(score)
        
    answer = []
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i+1)
    return answer