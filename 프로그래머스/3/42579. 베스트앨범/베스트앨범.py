def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] = [dic[genres[i]][0] + plays[i], 
                              dic[genres[i]][1] + [(plays[i], i)]]
            
        else:
            dic[genres[i]] = [plays[i], [(plays[i], i)]]        
            
    dic = sorted(dic.items(), key=lambda x:x[1][0], reverse=True)
    for genre, value in dic:
        value[1].sort(key=lambda x:x[0], reverse=True)
        
    answer = []
    
    for genre, value in dic:        
        answer.append(value[1][0][1])
        if len(value[1]) >= 2:            
            answer.append(value[1][1][1])
    
    return answer


