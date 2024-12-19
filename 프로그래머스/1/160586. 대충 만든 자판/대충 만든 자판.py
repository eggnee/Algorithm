def solution(keymap, targets):
    answer = []
    for i in targets: # i = ABCD
        click = 0
        
        for j in i: # A
            minClick = 101
            
            for k in keymap: # 최소 클릭 수 찾기 ABACD
                if j in k:
                    minClick = min(minClick, k.index(j)+1)
                    
            if minClick != 101:  # 클릭이 가능하다면
                click += minClick
            else: # 클릭이 불가하다면
                answer.append(-1)
                click = 0
                break
                
        if click != 0:
            answer.append(click)
    return answer