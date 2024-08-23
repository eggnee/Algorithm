def solution(price, money, count):
    hap = 0
    for i in range(1, count+1):
        hap += i * price
    answer = hap - money
    if answer > 0 :
        return answer
    else:
        return 0