M, N = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort()

answer = 0
start = 1
end = snack[-1]

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        break
    if sum(s // mid for s in snack) >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)