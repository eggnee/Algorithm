def solution(number, limit, power):
    answer = 0
    kg = []
    for i in range(1, number+1):
        cnt=0
        for j in range(1, int(i**0.5)+1):
            if(i % j == 0):
                cnt += 2
                if j**2 == i: 
                    cnt-=1
            if cnt > limit:
                cnt = power
                break
        kg.append(cnt)
    return sum(kg)