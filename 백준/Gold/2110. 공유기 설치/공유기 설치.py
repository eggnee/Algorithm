import sys

N, C = map(int, input().split())
points = []

for _ in range(N):
    points.append(int(sys.stdin.readline()))

points.sort()

def check(n):
    num = 1
    current = points[0]
    for i in range(1, N):
        if points[i] >= current + n:  # 현재 설치된 공유기와 n 이상의 거리 차이가 있으면 설치
            num += 1
            current = points[i]

        if num >= C:  # 공유기 개수 만족하면 바로 반환
            return num

    return num

dis = 1
start = 1
end = points[-1]

while start <= end:
    mid = (start + end) // 2
    if check(mid) < C:
        end = mid - 1
    else:
        start = mid + 1
        dis = mid

print(dis)
    