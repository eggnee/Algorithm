import sys
n, m = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

answer = 0
start = 0
end = trees[-1]
while True:
    if start > end:
        break
    mid = (start + end) // 2
    result = 0
    
    for i in trees:
        if i > mid:
            result += (i - mid)
            
    if result >= m:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)