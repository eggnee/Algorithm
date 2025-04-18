import math
from itertools import permutations

def solution(numbers):
    # 종이 조각을 붙여 만들 수 있는 소수의 개수
    # 최대 길이 7
    # 숫자 9999999까지 검사
    def check(number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
    answer = 0
    num_list = []
    
    for i in range(1, len(numbers) + 1):
        num_list += list(permutations(list(numbers), i))
        
    num_list = set(list(map(lambda x:int(''.join(x)), num_list)))
    
    for temp in num_list:
        if check(temp):
            answer += 1
            print(temp)

    return answer