def solution(arr):
    answer = []
    for temp in arr:
        if answer and answer[-1] == temp:
            continue
        answer.append(temp)
    return answer
            