import sys
n, m = map(int, input().split())
trees = list(map(int, input().split()))

answer = 0
start = 0
end = max(trees)

while True:
    if start > end:
        break
    
    mid = (start + end) // 2
    
    result = 0
    for i in trees:
        if i > mid:
            result += (i - mid)
            
    if result >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)