import sys
input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))

x = int(input())
a, b = 0, n-1
answer = 0

while(a<b):
    hap = num[a] + num[b]
    if hap == x:
        answer += 1
        a += 1
        b -= 1
    elif hap < x:
        a += 1
    else:
        b -= 1

print(answer)
