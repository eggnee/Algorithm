import sys
from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
points = list(map(int, sys.stdin.readline().split()))
points.sort()

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(bisect_right(points, end) - bisect_left(points, start))