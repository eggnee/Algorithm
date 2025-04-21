def solution(numbers, target):
    
    def dfs(now, i):
        if i == len(numbers) - 1:
            if now == target:
                return 1
            return 0
        
        i += 1
        return dfs(now + numbers[i], i) + dfs(now - numbers[i], i)
        
    return dfs(numbers[0], 0) + dfs(-numbers[0], 0)