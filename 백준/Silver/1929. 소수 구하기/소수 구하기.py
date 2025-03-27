M, N = map(int, input().split())

arr = set([i for i in range(M, N+1)])

for i in range(2, N):
    for j in range(2, (N // i) + 1):
        arr.discard(i * j)

arr.discard(1)

for i in arr:
    print(i)