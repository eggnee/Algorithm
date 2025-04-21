def solution(N, number):
    num_list = [set([int(str(N) * (i+1))]) for i in range(8)]
    
    for i in range(8):
        if number in num_list[i]:
            return i + 1
        for j in range(i):
            for op1 in num_list[j]:
                for op2 in num_list[i - j - 1]:
                    num_list[i].add(op1 + op2)
                    num_list[i].add(op1 - op2)
                    num_list[i].add(op1 * op2)
                    
                    if op2 != 0:
                        num_list[i].add(op1 // op2)
                
                    if number in num_list[i]:
                        return i + 1
    return -1