A, B = map(int, input().split())


def solution(number):
    num = 1
    answer = 0
    i = 0
    for _ in range(number):
        answer += num
        i += 1
        if num == i:
            num += 1
            i = 0
    return answer

print(solution(B) - solution(A-1))