import heapq
import sys


heap = []
n = int(input())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == '0':
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, int(cmd))