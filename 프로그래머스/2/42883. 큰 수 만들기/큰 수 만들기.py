def solution(number, k):   
    stack = []    
    n = len(number) - k
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        
        if k < 0:
            break
            
        stack.append(num)          
    
            
    if k > 0:
        stack = stack[:-k]
    
    return  ''.join(stack)
