N = int(input())
answer = 1
for i in range(N):
    answer = answer * (i+1)

if N == 0:
    print(1)
else:
    print(answer)