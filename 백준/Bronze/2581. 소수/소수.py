import math

m = int(input())
n = int(input())

num = [True for i in range(10001)]
num[0] = False
num[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if num[i] == True:
        j = 2
        while i * j <= n:
            num[i*j] = False
            j += 1
            
answer = []
for i in range(m, n+1):
    if num[i] == True:
        answer.append(i)
        
if len(answer) > 0:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)