import itertools, math

def solution(nums):
    answer = 0
    sumList = itertools.combinations(nums, 3)
    for j in sumList:
        sosu = True
        testNumber = sum(j)
        for k in range(2, int(math.sqrt(testNumber)) + 1):
            if testNumber % k == 0:
                sosu = False
                break  
        if sosu == True:
            answer += 1
    return answer