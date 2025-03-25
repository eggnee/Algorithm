from functools import cmp_to_key

def compare(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    else:
        return 1

def solution(numbers):
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(map(str, numbers))))



