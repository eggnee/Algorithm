# 길이가 n미터인 벽을 덧칠하기로 함
# 일부만 칠하기 위해 
# 1미터 구역을 n개로 나누고 n번까지 번호를 붙임
# 롤러의 길이 m 미터, 딱 벽의 좌우측 끝에 맞아야 함
# 2, 3, 4, 6 2 + 4 = 6
# 2부터 시작해서 m 길이만큼 section에 있다면 제거

def solution(n, m, section):
    answer = 0
    start = 0
    for i in section:
        if start <= i:
            answer += 1
            start = i + m
    return answer