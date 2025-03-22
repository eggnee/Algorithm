N = int(input())
arr = list(map(int, input().split()))

start, end = 0, N-1 
cha = abs(0 - (arr[start] + arr[end]))
a, b = start, end

while start < end:
    hap = arr[start] + arr[end]
    
    if cha > abs(0 - hap):
        a, b = start, end
        cha = abs(0 - hap)
    
    if hap > 0:
        end -= 1
    else:
        start += 1
        
print(arr[a], arr[b])

