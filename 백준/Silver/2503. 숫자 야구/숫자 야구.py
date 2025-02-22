from itertools import permutations
n = int(input())
nums = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))


for _ in range(n):
    answer, s, b = map(int, input().split())
    tmp = []
    
    answer = str(answer)
    for num in nums:
        
        strike = 0
        ball = 0
        
        for i in range(3):
            if num[i] in answer:
                if num[i] == answer[i]:
                    strike += 1
                else:
                    ball += 1
        
        if s == strike and b == ball:
            tmp.append(num)
    nums = tmp

print(len(nums))
