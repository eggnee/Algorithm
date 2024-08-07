def solution(x):
    hap = sum(map(int, list(str(x))))      
    if x % hap == 0:
        return True
    return False