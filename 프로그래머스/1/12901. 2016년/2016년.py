def solution(a, b):
    dayNumber = 0
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    monthdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a-1):
        dayNumber += monthdays[i]
    dayNumber += b
    answer = day[dayNumber % 7]
    return answer