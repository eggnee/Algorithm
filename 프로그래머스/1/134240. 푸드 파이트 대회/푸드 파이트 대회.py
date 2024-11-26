# [물의 개수 1로 고정, 1 음식의 개수, 2 음식의 개수, 3 음식의 개수...]


def solution(food):    
    food = food[1:]    
    answer = ''
    for i in range(len(food)):
        answer += str(i+1) * (food[i] // 2)
    return answer + "0" + answer[::-1]