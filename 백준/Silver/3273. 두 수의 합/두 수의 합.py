import sys
input = sys.stdin.readline

answer = 0
n = int(input())
num = []

for i in list(map(int, input().split())):
    num.append(i)
num.sort()

x = int(input())
a = 0
b = n-1

while(True):
    hap = num[a] + num[b]
    if hap == x:
        answer += 1
        a += 1
        b -= 1
    elif hap < x:
        a += 1
    else:
        b -= 1
    if a >= b:
        break

print(answer)
