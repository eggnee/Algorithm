import sys

N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()    
    
start = 0
end = arr[-1]
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    if mid != 0:
        for temp in arr:
            if temp != 0:
                cnt += (temp // mid)
                if cnt >= K:
                    break
    
    if cnt >= K:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

if K == 1:
    print(arr[-1])
else:
    print(answer)
    