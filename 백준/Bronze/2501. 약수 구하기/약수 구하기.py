n, k = map(int, input().split())
result = False
num = 1
for i in range(1, n+1):
    if n % i == 0:
        if num == k:
            print(i)
            result = True
            break
        num += 1
if result == False:
    print(0)